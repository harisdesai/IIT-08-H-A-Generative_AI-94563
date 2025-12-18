from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

convo = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    user_msg = {"role": "user", "content": user_input}
    convo.append(user_msg)
    llm_output = llm.invoke(convo)
    print("AI:", llm_output.content)
    llm_msg = {"role": "assistant", "content": llm_output.content}
    convo.append(llm_msg)