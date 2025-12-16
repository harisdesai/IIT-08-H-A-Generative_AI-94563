import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
def get_gemini_response(prompt):
    api_key = os.getenv("GEMINI_API_URL")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"

    flag = True
    while flag:
        if prompt == "exit":
            flag = False
        else:
            headers = {
                "Content-Type": "application/json"
            }
            data = { "contents":[{"parts":[{"text":prompt}]}]
            }

            response = requests.post(url, headers=headers, json=data)

            reply = response.json()

            gemini_response = reply["candidates"][0]["content"]["parts"][0]["text"]

            return gemini_response