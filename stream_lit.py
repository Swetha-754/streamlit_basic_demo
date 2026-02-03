import os
from langchain_community.chat_models import ChatOllama
import streamlit as st 
from langchain_core.globals import set_debug
set_debug(True)

llm=ChatOllama(model="llama3.2:3b")
st.title("Ask anything")
question=st.text_input("Enter a question:")
if question:
    response=llm.invoke(question)
    st.write(response.content)