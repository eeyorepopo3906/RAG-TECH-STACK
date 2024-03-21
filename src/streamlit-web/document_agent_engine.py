import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import sys
sys.path.append("..")

#from local_models.llm import MyLLM, LlamaCPPLLM
from llama_index.llms.openai import OpenAI
from local_models.embeddings import get_embed_model
from llama_index.core import ServiceContext

from data_loader.parsing import MDDF
from data_loader.splitting import split_by_md_headers, text_2_Document
from data_loader.chunking import chunk_docs_standalone
from data_loader.load_from_dir import rebuild_index


#from llama_index.core import Document
import os, re
import pandas as pd

from typing import Dict, List
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core import PromptTemplate
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.schema import IndexNode

from llama_index.agent.openai import OpenAIAgent
#from llama_index.core.agent import ReActAgent

from llama_index.core.retrievers import RecursiveRetriever
from llama_index.core.response_synthesizers import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine

from utils import load_prompt
import logging

load_dotenv(override=True)
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

mappings = {
    '第一部分': '公共规则：范围、规范性饮用文件、属于和定义、总则、作业基本条件及要求、保证安全的组织措施、保证安全的技术措施、设备巡视、设备操作',
    '第二部分': '常规作业：单一类型作业、带电作业、邻近带点体作业、二次设备作业、架空线路作业、电力电缆作业、高/低压配电网作业',
    '第三部分': '专项作业：试验作业、电气测量作业、水轮机作业、高处作业、密封空间作业、水域作业、焊接及切割作业、动火作业、起重与运输',
    '第四部分': '工器具：安全工器具、带电作业工具、施工机具、电器工具及一般工具',
}


@st.cache_resource
def build_doc_agent_engine(similarity_top_k=2): #key_words, docs=None, 
    logger.info('loading llm and embed_model...')
    embed_model = get_embed_model(model_name=os.environ['embed_path'],  model_kwargs={'device': 'cpu'}, encode_kwargs = {'normalize_embeddings': True})

    llm = OpenAI(temperature=0)
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)


    logger.info('loading prompt...')
    #load prompt
    prompt_str = load_prompt('../../prompt_bank/safety_practice.txt')
    new_vector_tmpl = PromptTemplate(prompt_str)


    logger.info('building doc agent for each doc')
    ##Build Document Agent for each Document
    num_docs = 4#len(documents)

    #build agents dict
    agents = {}
    nodes = []
    for i in range(num_docs):
        
        #load from disk
        vector_index = rebuild_index(persist_dir=f'../../db_stores/doc_agent_vector_index/idx_{i}', service_context=service_context)
        fn = list(vector_index.ref_doc_info.values())[0].metadata['file_name'].split('.')[0]




        #load from disk
        summary_index = rebuild_index(persist_dir=f'../../db_stores/doc_agent_summary_index/idx_{i}', service_context=service_context)



        #define query engines
        vector_query_engine = vector_index.as_query_engine(llm=llm)
        vector_query_engine.update_prompts({'response_synthesizer:text_qa_template': new_vector_tmpl})
        
        #kw_query_engine = kw_index.as_query_engine()
        list_query_engine = summary_index.as_query_engine(llm=llm)
        list_query_engine.update_prompts({'response_synthesizer:text_qa_template': new_vector_tmpl})

        #define tools
        query_engine_tools = [
            QueryEngineTool(
                query_engine=vector_query_engine,
                metadata=ToolMetadata(
                    name="vector_tool",
                    description=(
                        f"Useful for retrieving specific context from {fn}"
                    )
                )
            ),
            QueryEngineTool(
                #query_engine=kw_query_engine,
                query_engine=list_query_engine,
                metadata=ToolMetadata(
                    name="summary_tool",
                    description=(
                        f"Useful for summarization-wise questions about {fn}"
                    )
                )
            )
        ]
        

        #build agents
        agent = OpenAIAgent.from_tools(
            query_engine_tools,
            llm=llm,
            embed_model=embed_model,
            verbose=True,
            
            
            system_prompt=f"""\
                Make sure to respond in Chinese.

                You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.

                Please refer to the summary_tool first if you inquire summarization-wise questions about{mappings[fn]},

                If you need to fetch details about {mappings[fn]}, please refer to the vector_tool first.
                """,
        )
        agents[fn] = agent
    
    
        ##Build Composable Retriever over the agents
        #define top-level nodes
        instru =(
            f"This content contains instructions on safety practice regarding {mappings[fn]}, "
            f"Use this index if you need to look up specific facts about {mappings[fn]}, "
            f"Do not use this index if you want to analyze aspects beyond {mappings[fn]} "

        )

        node = IndexNode(
            text=instru, index_id=fn, obj= agent
            )
        nodes.append(node)
    
    #define top-level retriever
    top_vector_index = VectorStoreIndex(objects=nodes, embed_model=embed_model)
    query_engine = top_vector_index.as_query_engine(similarity_top_k=similarity_top_k, verbose=True)

    logger.info('Done...')
    return query_engine