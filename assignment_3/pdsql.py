import streamlit as st
import pandas as pd
from pandasql import sqldf
csv_file = st.file_uploader(label="upload a file",type=["csv"])
if csv_file is not None:
    df = pd.read_csv(csv_file)
    data = df
    st.dataframe(df)
    user_input = st.chat_input("Ask Anything about this CSV : ")
    if user_input:
        query = str(user_input)
        result2 = sqldf(query, globals())
        st.write("Result : ")
        st.write(result2)