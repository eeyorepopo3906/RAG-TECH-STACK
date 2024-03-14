import warnings
warnings.filterwarnings('ignore')
import streamlit as st

import sys
sys.path.append("..")
from nebula_graph.text_2_graph import df_to_fig, extract_triplets, get_response_n_kg_rel_query
################Import Modules##################
from engine_types import table, document_agent, kgi
from table_engine import build_table_n_text_engine
from document_agent_engine import build_doc_agent_engine
from graph_rag_engine import build_graph_rag_engine
################################################
from dotenv import load_dotenv
import os, io, sys, traceback
import time


load_dotenv(override=True)

class OutputCapture:
    def __init__(self):
        self.buffer = io.StringIO()

    def isatty(self):
        return False

    def write(self, message):
        self.buffer.write(message)

    def flush(self):
        pass

    def get_output(self):
        return self.buffer.getvalue()
    
SHOW_TRACE_ON_UI = True

def process_query(prompt):
    captured_output_str = "No trace available!"
    response = ""
    try:
        if SHOW_TRACE_ON_UI:
            captured_output = OutputCapture()
            sys.stdout = captured_output
        response = st.session_state.chat_engine.query(prompt)
        if SHOW_TRACE_ON_UI:
            sys.stdout = sys.__stdout__

        if SHOW_TRACE_ON_UI and captured_output is not None:
            captured_output_str = captured_output.get_output()
            
    except Exception as e:
        response = f"Error:\n{str(e)}"
        traceback.print_exc()
    return (response, captured_output_str)



def execute_with_timeout(function, timeout=20):
    start_time = time.time()
    end_time = start_time + timeout

    while time.time() < end_time:
        try:
            function()  # Execute the function
            return   # Return the result if successful
        except Exception as e:
            # Handle any specific exceptions if needed
            pass
    st.warning("Encountering connection error...Please wait a few seconds and retry later")

    # Raise an exception if the function did not succeed within the timeout
    




with st.sidebar:
    st.markdown(
        "### 主要参数说明 \n"
        "1. LLM: gpt-3.5-turbo \n"
        "2. Embeddings: moka-ai/m3e-base"
        "`(适用场景：中文为主、少量英文｜不适合代码检索场景)`\n"
        "3. Document(s): KDP-WhitePaper.md"
        "`(文本特征：偏通用型、含有少量`:blue[table]`、不含`:blue[code block]`)` \n"
    )

st.header("Check out what's inside KDP Whitepaper:books:")



engine = st.selectbox("query engine", (table, document_agent, kgi))


if engine == table:
    st.session_state.chat_engine = build_table_n_text_engine()
    
elif engine== document_agent:
    st.session_state.chat_engine = build_doc_agent_engine()
    
else:
    st.session_state.chat_engine = build_graph_rag_engine()
    
#st.write(st.session_state.chat_engine)
    


def wrapper():
    #resp = st.session_state.chat_engine.chat(prompt)
    resp, captured_output_str = process_query(prompt)

    if engine=='graph rag(kgi-based)':
        kg_rel_texts = get_response_n_kg_rel_query(resp)[1]
        if kg_rel_texts:
            extracted_triplets = extract_triplets(kg_rel_texts)
            kg_fig = df_to_fig(extracted_triplets, show_fig=False)
            st.pyplot(kg_fig)

    
    response = resp.response
    
    st.text_area("Response", response, height=2, max_chars=100)
    debug_info = st.sidebar.empty()
    if captured_output_str != '':
        debug_info.text_area("Intermediate Generated Instructions", captured_output_str, height=600)

    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)



if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "有什么能够帮到您？"}]



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking ... "):
            execute_with_timeout(wrapper, timeout=20)



        
        
        

        
