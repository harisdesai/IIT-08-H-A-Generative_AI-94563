import streamlit as st
import login_form
import weatherr

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    weatherr.weather_application()
    login_form.logout()

else:
    login_form.login()

