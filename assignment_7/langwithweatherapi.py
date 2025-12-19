from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
import streamlit as st
import requests
from dotenv import load_dotenv
load_dotenv()

st.session_state['page'] = 'Weather with LLM Explanation'
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

if "explanation" not in st.session_state:
    st.session_state.explanation = ""

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
st.title("Weather App")
city = st.text_input("Enter city name:")
if st.button("Get Weather"):
    if city:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            st.session_state.weather_data = response.json()
            st.session_state.explanation = ""
        else:
            st.error("City not found. Please check the city name and try again.")
    else:
        st.warning("Please enter a city name.")

if st.session_state.weather_data:
    data = st.session_state.weather_data
    st.subheader(f"Weather in {city}")
    st.write(f"Temperature: {data['main']['temp']} °C")
    st.write(f"Weather: {data['weather'][0]['description']}")
    st.write(f"Humidity: {data['main']['humidity']}%")
    st.write(f"Wind Speed: {data['wind']['speed']} m/s")

# llm_url = "http://127.0.0.1:1234/v1"
# llm = ChatOpenAI(
#     base_url=llm_url,
#     model = "microsoft/phi-4-mini-reasoning",
#     api_key="123456789"
# )

api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-120b",api_key=api_key)

if st.button("Get Explanation"):
    if city and st.session_state.weather_data:
        prompt = f"""
        The current weather information is:
        Temperature: {data['main']['temp']} degree Celsius,
        Condition: {data['weather'][0]['description']},
        Humidity: {data['main']['humidity']} percent,
        Wind Speed: {data['wind']['speed']} meters per second.

        Explain this current weather in simple English,
        easy for beginners to understand.Single paragraph only.
        """
        result = llm.stream(prompt)
        explanation = ""
        for chunk in result:
            explanation += chunk.content
        st.session_state.explanation = explanation
    else:
        st.warning("Get weather first.")

if st.session_state.explanation:
    st.subheader("LLM Explanation")
    st.write(st.session_state.explanation)