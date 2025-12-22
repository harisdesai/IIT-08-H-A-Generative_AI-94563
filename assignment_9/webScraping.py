import streamlit as st
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def WebScrapingApp():
    st.header("Web Scraping Agent – Sunbeam Internships")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask about Sunbeam internships")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        keyword_prompt = f"""
        Extract important search keywords from the following question.
        Return only comma-separated keywords. No explanation.

        Question: {user_input}
        """

        keyword_response = llm.invoke(keyword_prompt)
        keywords = [k.strip().lower() for k in keyword_response.content.split(",")]

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10)

        driver.get("https://www.sunbeaminfo.in/internship")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        rows = driver.find_elements(By.TAG_NAME, "tr")
        results = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_text = " ".join(c.text.lower() for c in cols)

            if any(k in row_text for k in keywords):
                results.append([c.text for c in cols])

        driver.quit()

        with st.chat_message("assistant"):
            if results:
                st.subheader("Matching Internship Details")
                for r in results:
                    st.write(" | ".join(r))
                    st.divider()

                response_text = (
                    f"I extracted keywords ({', '.join(keywords)}) "
                    f"and found relevant internship information from Sunbeam."
                )
            else:
                st.warning("No matching data found.")
                response_text = (
                    "I understood your question, but no matching internship "
                    "information was found on the Sunbeam website."
                )

            st.markdown(response_text)

        st.session_state.messages.append(
            {"role": "assistant", "content": response_text}
        )

WebScrapingApp()
