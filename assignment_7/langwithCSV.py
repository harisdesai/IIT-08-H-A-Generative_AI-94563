import streamlit as st
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)


csv_file =  st.file_uploader("Upload a CSV file", type=["csv"])
if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.write("CSV schema: ")
    st.dataframe(df)
    user_input = st.chat_input("Ask anything about this CSV? ")
    if user_input:
        llm_input = f"""
            Table Name: data
            Table Schema: {df}
            Question: {user_input}
            Instruction:
                Write a SQL query for the above question. 
                Generate SQL query only in plain text format and nothing else.
                If you cannot generate the query, then output 'Error'.
        """
        result = llm.invoke(llm_input)
        st.write(result.content)
