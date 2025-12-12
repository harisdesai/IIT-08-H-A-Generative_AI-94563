import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
with open("posts.txt", "w") as f:
    json.dump(data, f, indent=4)
print("Data has been fetched from the API and saved to posts.json")
print(data)

