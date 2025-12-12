import requests
import json

api_key = "fcf790d6e81b5c3b76c3e8fa411c0721"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
try:
    response = requests.get(url)
    data = response.json()
    print("Temperature Data:", data["main"]["temp"])
    print("Weather Description:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"])
    print("Wind Speed:", data["wind"]["speed"])
except Exception as e:
    print("An error occurred:", e)    