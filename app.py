import streamlit as st
from graph import graph
from dotenv import load_dotenv

load_dotenv()

st.title("AI Blog Generator using LangGraph")

topic = st.text_input("Enter Blog Topic")

if st.button("Generate Blog"):

    with st.spinner("Generating blog..."):

        result = graph.invoke({"topic": topic})

        st.markdown(result["final_blog"])