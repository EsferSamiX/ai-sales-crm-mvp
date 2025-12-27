from langchain_groq import ChatGroq
import os

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    groq_api_key=groq_api_key,
    temperature=0.3
)
