import streamlit as st
import os
from dotenv import load_dotenv
import chattbot as chatbot_module
load_dotenv()

st.title("🤖 Chatbot Interface")

prompt = st.chat_input("Type your message here...")
st.session_state.setdefault("messages", [])
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = chatbot_module.get_gemini_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
    

