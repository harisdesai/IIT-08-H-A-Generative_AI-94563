import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

@tool
def calculator(expression):
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Cannot solve expression"

@tool
def get_weather(city):
    """
    This get_weather() function gets the current weather of given city.
    If weather cannot be found, it returns 'Error'.
    This function doesn't return historic or general weather of the city.

    :param city: str input - city name
    :returns current weather in json format or 'Error'    
    """
    try:
        api_key = os.getenv("API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"

@tool
def read_file(filepath):
    """reads the content of a text file given its filepath and returns the content as a string."""
    with open(filepath, 'r') as file:
        text = file.read()
        return text
    
llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

conversation = []
agent = create_agent(
    model=llm,
    tools=[calculator, get_weather, read_file],
    system_prompt="You are a helpful assistant. Answer in short."
)
# Streamlit UI with session state
st.title("Agent Chat with Groq")
if "conversation" not in st.session_state:
    st.session_state.conversation = []
prompt = st.chat_input("Enter your message")
if prompt:
    st.session_state.conversation.append(HumanMessage(content=prompt))
    result = agent.invoke({"messages": st.session_state.conversation})
    st.session_state.conversation = result["messages"]
for msg in st.session_state.conversation:
    if msg.type in ("human", "ai") and msg.content.strip():
        st.chat_message(msg.type).write(msg.content)
