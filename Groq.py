import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.0,
    api_key = os.getenv("GROQ_API_KEY")
)

response = llm.invoke("Why latency needs to be reduced in AI applications?")
print(response.content)