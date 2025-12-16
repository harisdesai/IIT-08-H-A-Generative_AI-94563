import streamlit as st

st.title("ChatBot")
st.sidebar.title("ChatBot Settings")
st.sidebar.markdown("Adjust the settings for your chatbot below.")
st.sidebar.slider("Response Length", min_value=10, max_value=200, value=100, step=10)
st.sidebar.selectbox("Tone", options=["Formal", "Casual", "Humorous"], index=0)
st.text_area("User Input", height=100, placeholder="Type your message here...")
st.button("Send")
st.markdown("### Chat History")
st.markdown("_No messages yet._")
st.markdown("This is a simple chatbot interface built with Streamlit.")
st.markdown("Feel free to customize the settings and start chatting!")




    