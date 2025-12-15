import streamlit as st
import pandas as pd

def login():
    st.title("Login Form")

    if "logout_message" in st.session_state:
        st.info(st.session_state["logout_message"])
        del st.session_state["logout_message"]

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Login successful!")
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Invalid username or password.")

def logout():
    if st.button("Logout"):
        st.session_state["logout_message"] = "You have been logged out."
        st.session_state['logged_in'] = False
        st.rerun()
