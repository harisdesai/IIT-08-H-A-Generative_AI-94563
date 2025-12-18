from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_URL")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    result = llm.stream(user_input)
    for chunk in result:
        print(chunk.content,end="")