from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

llm_url = "http://127.0.0.1:1234/v1"
llm = ChatOpenAI(
    base_url=llm_url,
    model = "microsoft/phi-4-mini-reasoning",
    api_key="123456789"
)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    result = llm.stream(user_input)
    for chunk in result:
        print(chunk.content,end="")