import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load local .env (ignored if it doesn't exist)
load_dotenv()

# Read the API key from the environment
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Configure it in your local .env or in Streamlit Secrets."
    )

llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)