import streamlit as st
import groq as g
import oi4mini as phi
import time
from dotenv import load_dotenv
load_dotenv()

if "page" not in st.session_state:
    st.session_state.page = "groq"

if "msg_groq" not in st.session_state:
    st.session_state.msg_groq = []

if "msg_local" not in st.session_state:
    st.session_state.msg_local = []

st.title("Chat with Language Models")
with st.sidebar:
    if st.button("Groq LLM", use_container_width=True):
        st.session_state.page = "groq"
    if st.button("OI4Mini LLM", use_container_width=True):
        st.session_state.page = "oi4mini"

if st.session_state.page == "groq":
    prompt = st.chat_input("enter your message")

    if prompt:
        st.session_state.msg_groq.append({
            "role" : "user",
            "content": prompt
        })

        response = g.get_groq_response(prompt)

        st.session_state.msg_groq.append({
            "role" : "assistant",
            "content": response
        })

    for msg in st.session_state.msg_groq:
        st.chat_message(msg["role"]).write(msg["content"])


if st.session_state.page == "oi4mini":
    prompt = st.chat_input("enter your message")

    if prompt:
        st.session_state.msg_local.append({
            "role" : "user",
            "content": prompt
        })

        response = phi.get_oi4mini_response(prompt)

        st.session_state.msg_local.append({
            "role" : "assistant",
            "content": response
        })

    for msg in st.session_state.msg_local:
        st.chat_message(msg["role"]).write(msg["content"])
    