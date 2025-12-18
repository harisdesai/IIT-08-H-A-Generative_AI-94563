from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-120b",api_key=api_key)
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    result = llm.stream(user_input)
    for chunk in result:
        print(chunk.content,end="")
    