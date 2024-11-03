import streamlit as st
import re
from PyPDF2 import PdfReader

def clean_text(text):
    # Replace multiple newlines with a single newline to avoid excessive line breaks
    text = re.sub(r'\n{2,}', '\n', text)

    # Add an extra newline after recognized section headers or bulleted points to separate them
    text = re.sub(r'(•|Projects|EXPERIENCE|EDUCATION|SKILLS)', r'\n\1', text)

    # Attempt to merge lines that are part of the same sentence
    text = re.sub(r'(?<=\w)\n(?=\w)', ' ', text)
    return text


def main():
    st.title('Cover Letter Builder')

    #uploading a pdf file
    pdf = st.file_uploader("Please submit your resume",type='pdf')
    
    text = " "
    
    

    if pdf:
        resume = PdfReader(pdf)
        """st.write(resume)"""
        #printing the uploaded resume
        
        for page in resume.pages:
            page_text = page.extract_text()
            text += page_text + "\n\n"
        text = clean_text(text) 
        st.write(text)
if __name__ == "__main__":
    main()
    



