# Cover Letter Builder

## 📌 Overview
The **Cover Letter Builder** is a Generative AI-powered application built using **Streamlit**, **LangChain**, and **Groq Llama3-8b**. This tool generates tailored cover letters based on the provided resume and user instructions. By analyzing the resume content and extracting relevant experiences, it creates a domain-specific cover letter, enhancing job application personalization.

## 🚀 Features
- 📄 **Upload Resume**: Users can upload a PDF resume.
- ✍ **Custom Instructions**: Users can provide additional instructions for customization.
- 🏢 **Company-Specific Personalization**: Extracts the company name from the instructions and tailors the cover letter accordingly.
- 🤖 **AI-Powered Generation**: Utilizes **Groq's Llama3-8b** model to generate high-quality cover letters.
- 🎯 **Domain-Specific Optimization**: Highlights relevant experiences matching the company's industry.
- 🖥 **Streamlit UI**: Simple and intuitive web interface.

## 📂 Project Structure
```
├── frontend.py       # Streamlit app handling file upload & UI
├── groq.py          # LLM-based cover letter generation
├── Agent.py         # Extracts company name from user instructions
├── requirements.txt # Project dependencies
├── .env             # Stores API keys (not included in repo)
└── README.md        # Documentation
```

## 🔧 Setup & Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/CoverLetterBuilder.git
   cd CoverLetterBuilder
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up API key**
   - Create a `.env` file in the root directory.
   - Add the following line:
     ```sh
     GROQ_API_KEY=your_api_key_here
     ```
4. **Run the application**
   ```sh
   streamlit run frontend.py
   ```

## 🛠️ Code Explanation

### 1️⃣ `frontend.py` (Streamlit Frontend)
```python
st.title('Cover Letter Builder')

pdf = st.file_uploader("Please submit your resume", type='pdf')
User_Instructions = st.text_area("Enter Instructions", placeholder="Please enter organization name...")

Organization_Info = extract_company_name_with_ner(User_Instructions)

if st.button("Generate Cover Letter"):
    if pdf:
        pdf_reader = PdfReader(pdf)
        text = " ".join([page.extract_text() for page in pdf_reader.pages])
        CoverLetter = Generate_Cover_Letter(text, User_Instructions, Organization_Info)
        st.write(CoverLetter.content)
    else:
        st.warning('Please Enter Resume', icon="⚠️")
```
- **Handles File Upload**: Users can upload a PDF resume.
- **Takes User Instructions**: Users enter preferences to customize their cover letter.
- **Calls AI Model**: Sends resume text and instructions to `Generate_Cover_Letter`.
- **Displays Generated Cover Letter**: Shows AI-generated output in the UI.

### 2️⃣ `groq.py` (AI Cover Letter Generation)
```python
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.0,
    api_key=os.getenv("GROQ_API_KEY")
)

def Generate_Cover_Letter(Uploaded_pdf, Instructions, Organization_Info):
    Input_prompt = PromptTemplate.from_template("""
    Write a cover letter based on the resume: {Uploaded_pdf},
    user instructions {Instructions}, and organization info {Organization_Info}.
    If the resume includes relevant projects or experiences in the organization's domain, highlight them.
    If the organization's industry isn't clear, focus on the user's suitability for the job role.
    (NO PREAMBLE)
    """)
    
    chain_llm = Input_prompt | llm
    response = chain_llm.invoke(input={"Uploaded_pdf": Uploaded_pdf, "Instructions": Instructions, "Organization_Info": Organization_Info})
    return response
```
- **Uses LangChain-Groq Llama3-8b** for AI-powered text generation.
- **Processes Resume & Instructions**: Extracts job-relevant details and company info.
- **Tailors Cover Letter to Job Domain**: Highlights experiences related to the employer’s industry.

### 3️⃣ `Agent.py` (Company Name Extraction)
- Extracts the organization name from user instructions.
- Helps in creating industry-specific cover letters.

## 📜 Example Usage
1. Upload a resume (PDF format).
2. Enter job-specific instructions (e.g., "Applying to Google as a Data Engineer").
3. Click "Generate Cover Letter".
4. The AI will create a tailored cover letter highlighting relevant experience.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributions
Feel free to submit pull requests or open issues for feature requests and improvements.

---
🚀 **Happy Job Hunting!**

