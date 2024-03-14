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




@st.cache_resource
def build_doc_agent_engine(similarity_top_k=2): #key_words, docs=None, 
    logger.info('loading llm and embed_model...')
    embed_model = get_embed_model(model_name=os.environ['embed_path'],  model_kwargs={'device': 'cpu'}, encode_kwargs = {'normalize_embeddings': True})
    #llm = MyLLM(pretrained_model_name_or_path=os.environ['llm_path'], device_map="mps", context_window=4096, num_output=512, model_name='chatglm3-6b')
    llm = OpenAI(temperature=0)
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)


    logger.info('formatting md as DF and splitting into separate docs...')
    #format md as DF
    df = split_by_md_headers('../../data/产品白皮书/KDP-WhitePaper.md')
    #construct node mappings
    key_words= MDDF(df, [1]).construct_node_mappings(show_progress=False)[0]#remove useless contents


    logger.info('loading prompt...')
    #load prompt
    prompt_str = load_prompt('../../prompt_bank/whitepaper.txt')
    new_vector_tmpl = PromptTemplate(prompt_str)


    logger.info('building doc agent for each doc')
    ##Build Document Agent for each Document 
    #build agents dict
    agents = {}
    nodes = []
    for i, kw in enumerate(key_words):

        #build vector index--first time
        #vector_index = VectorStoreIndex(docs[kw], embed_model=embed_model)
        #vector_index.storage_context.persist(persist_dir="db_stores/doc_agent_vector_index")

        #load from disk
        vector_index = rebuild_index(persist_dir=f'../../db_stores/doc_agent_vector_index/idx_{i}', service_context=service_context)


        #build keyword indexfirst time
        #kw_index = KeywordTableIndex.from_docunments(docs[kw])
        #summary_index = SummaryIndex(docs[kw], embed_model=embed_model)
        #summary_index.storage_context.persist(persist_dir="db_stores/doc_agent_summary_index")

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
                        f"Useful for retrieving specific context from {kw}"
                    )
                )
            ),
            QueryEngineTool(
                #query_engine=kw_query_engine,
                query_engine=list_query_engine,
                metadata=ToolMetadata(
                    name="summary_tool",
                    description=(
                        f"Useful for summarization-wise questions related to {kw}"
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
            #output_parser=output_parser, 
            
            system_prompt=f"""\
                Make sure to respond in Chinese.

                You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.

                Please refer to the summary_tool first if you inquire general-purpose questions about the {kw},
                for which a summary suffices.

                For questions involving specific facts, such as step-by-step instructions or troubleshooting issues, 
                please refer to the vector_tool first, as such questions demand a
                finer degree of information granularity.
                """,
        )#ReActAgent
        agents[kw] = agent
    
        
        ##Build Composable Retriever over the agents
        #define top-level nodes
        instru =(
            f"{kw} are the headers and subheaders corresponding to specific paragraphs from the KDP whitepaper, "
            "(To clarify, KDP stands for Kubernetes Data Platform, "
            "which is a enterprise-level big data platform developed by Linktime Cloud Co., Ltd.) "
            "You are a well-versed agent designed to answer queries about the following aspect of the KDP whitepaper, "
            f"{kw} "
            "and you know by heart the core concepts and mechanisms of big data technologies. "
            f"This paragraph contains contents associated with the topic {kw}. "
            "Use this index if you need to look up information about {kw}, "
            "Do not use this index if you want to gather information from multiple aspects beyond {kw}"
        )

        node = IndexNode(
            text=instru, index_id=kw, obj= agent
            )
        nodes.append(node)
    

    logger.info('constructing top-level retriever and then query engine...')
    #define top-level retriever
    top_vector_index = VectorStoreIndex(objects=nodes, embed_model=embed_model)
    query_engine = top_vector_index.as_query_engine(similarity_top_k=similarity_top_k, verbose=True)
    
    logger.info('Done...')
    #if "chat_engine" in st.session_state.keys():
        #st.session_state.clear()
        ##st.session_state.pop("chat_engine")
    
    #st.session_state.chat_engine = query_engine
    return query_engine