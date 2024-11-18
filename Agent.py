#extracting organization name from the given instructions and passing it to Wikipedia retriver to extract more information about the company
import spacy
from langchain_community.retrievers import WikipediaRetriever

nlp = spacy.load("en_core_web_sm")

def extract_company_name_with_ner(instructions):
    doc = nlp(instructions)
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Organization entities
            #return ent.text
            retriever = WikipediaRetriever()
            docs = retriever.invoke(ent.text)
            #print(docs[0].metadata.get('summary'))
            return docs[0].metadata.get('summary')
    return None
#instructions = "I am applying for a data engineer job at chevron pls generate a cover letter for the job based on the resume"
#print(extract_company_name_with_ner(instructions))  




