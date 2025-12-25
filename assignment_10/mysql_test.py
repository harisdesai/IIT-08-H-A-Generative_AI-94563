#Create a Streamlit web application that allows users to connect to a MySQL database and ask natural language questions. The app should generate and execute SELECT SQL queries using an LLM and display both the query results and a simple English explanation.

import mysql.connector
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

host = "localhost"     # or your MySQL server IP
user = "root"          # your MySQL username
password = "manager" # your MySQL password
database = "test_db"   # database to connect to


try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=True
    )

    st.title("MySQL Query App")

    st.success("Connected to MySQL database!")

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Example: Fetch tables
    cursor.execute("SHOW TABLES")
    tables = [c[0] for c in cursor.fetchall()]

    table_name = st.selectbox("Select a table to show details", tables)
    cursor.execute(f"SELECT * FROM {table_name}")
    details = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(details, columns=columns)
    st.dataframe(df)

    cursor.execute(f"DESCRIBE {table_name}")
    schema = cursor.fetchall()

    # Example: Fetch some data
    user_input = st.chat_input("Ask anything about this CSV? ")
    if user_input:
        llm_input = f"""
            Table Name: {tables}
            Table Schema: {tables}
            Question: {user_input}
            Instruction:
                Write a SQL query for the above question. 
                Generate SQL query only in plain text format and nothing else.
                If you cannot generate the query, then output 'Error'.
        """
        query = llm.invoke(llm_input)
        sql = query.content.strip()
        query_type = sql.split()[0].lower()
        st.info(query.content)
        if query.content == "Error":
            st.error("error in generating query")

        else:
                cursor.execute(sql)

                if query_type == "select":
                    result = cursor.fetchall()
                    columns = [col[0] for col in cursor.description]
                    df_result = pd.DataFrame(result, columns=columns)
                    st.subheader("Query Result")
                    st.dataframe(df_result)
                else:
                    st.success("Query executed successfully")
                    st.write(f"Rows affected: {cursor.rowcount}")
                    result = f"{cursor.rowcount} rows affected"

                prompt = f"""
                            user question: {user_input}
                            generated querry: {query.content}
                            result: {result}
                            task:
                            explain the result in simple english, 
                            dont use sql langauge, 
                            keep it understandable for some one who dont know sql at all.
                            """
                explanation = llm.invoke(prompt)
                st.write("Explanation")
                st.write(explanation.content)

except mysql.connector.Error as err:
    st.error(f"Error: {err}")
