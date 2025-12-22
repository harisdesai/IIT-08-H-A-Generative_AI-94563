from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

conversation = []

agent = create_agent(model=llm,tools=[], system_prompt="You are a helpful assistant. Answer in short.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    conversation.append({"role": "user", "content": user_input})
    result = agent.invoke({"messages": conversation})
    ai_msg = result["messages"][-1]
    print("AI: ", ai_msg.content)
    conversation = result["messages"]