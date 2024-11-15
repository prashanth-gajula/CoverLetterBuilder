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

def Generate_Cover_Letter(Uploaded_pdf,Instructions):
    
    #Prompt for LLM
    
    Input_prompt  = PromptTemplate.from_template("""
    Write a cover letter for a job application based on the resume: {Uploaded_pdf} and user instructions {Instructions}
    If the user mentioned about the organization that he is going to apply and if there are any projects that are related to 
    organization domain please talk about that project in the cover letter.
    For Example: if the user applying for a job in chevron since it is a oil and gas company please mention about 
    any petroleum project available in  resume and similarly for other organizations in other domain and 
    if you are unable to determine organization domain talk about the users ability for the job role base on the projects and experience available in the resume.
    (NO PREAMBLE) 
    """)
    #print("welcome to the project")
    chain_llm = Input_prompt | llm
    response = chain_llm.invoke(input={"Uploaded_pdf":Uploaded_pdf,"Instructions":Instructions})
    #print(response)
    return response
#response = llm.invoke("Why latency needs to be reduced in AI applications?")
#print(response.content)