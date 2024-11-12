import streamlit as st
import re
from PyPDF2 import PdfReader
from streamlit_pdf_viewer import pdf_viewer
#from Groq import llm
from Groq import Generate_Cover_Letter


def main():
    st.title('Cover Letter Builder')

    #uploading a pdf file
    pdf = st.file_uploader("Please submit your resume",type='pdf')
    
   

    if pdf:
        #Displaying the uploaded resume
        binary_data = pdf.getvalue()
        pdf_viewer(input=binary_data,width=700)
        #st.write("Cover Letter For the Uploaded Resume:")
        pdf_reader = PdfReader(pdf)
        text = " "
        for page in pdf_reader.pages:
            text +=page.extract_text()
        #st.write(text)
        CoverLetter = Generate_Cover_Letter(text)
        st.write(CoverLetter.content)
    
if __name__ == "__main__":
    main()
    



