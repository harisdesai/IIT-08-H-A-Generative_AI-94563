#create weather app using streamlit and openweathermap api
import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()   
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
            data = response.json()
            st.subheader(f"Weather in {city}")
            st.write(f"Temperature: {data['main']['temp']} °C")
            st.write(f"Weather: {data['weather'][0]['description']}")
            st.write(f"Humidity: {data['main']['humidity']}%")
            st.write(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            st.error("City not found. Please check the city name and try again.")
    else:
        st.warning("Please enter a city name.")