import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.0,
    api_key = os.getenv("GROQ_API_KEY")
)

def Generate_Cover_Letter(Uploaded_pdf):
    
    #Prompt for LLM
    
    Input_prompt  = PromptTemplate.from_template("""
    Write a cover letter for a job application based on the resume: {Uploaded_pdf}
    
    """)
    #print("welcome to the project")
    chain_llm = Input_prompt | llm
    response = chain_llm.invoke(input={Uploaded_pdf})
    #print(response)
    return response
#response = llm.invoke("Why latency needs to be reduced in AI applications?")
#print(response.content)