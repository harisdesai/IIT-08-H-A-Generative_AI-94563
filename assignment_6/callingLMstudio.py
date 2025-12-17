import json
import requests

api_key = "dummy-key"
url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model":"microsoft/phi-4-mini-reasoning",
    "messages":[
        {"role":"user","content":"Explain what quantization is in simple terms."}
    ]
}

response = requests.post(url,headers=headers,data=json.dumps(data))
print(response.json())