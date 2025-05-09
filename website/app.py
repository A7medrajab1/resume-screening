import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from resume_evaluator import evaluate_resume_against_jobs
from job_description_utils import extract_text_from_pdf, parse_job_descriptions,extract_job_titles


#######################################--Models--#######################################
llm_llama_4_maver = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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", 
    model="meta-llama/llama-4-maverick:free",
    temperature=0.0,
    name="Llama-4-Maverick"
)

llm_deepseek_R1 = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    model="deepseek/deepseek-r1:free",
    temperature=0.0,
    name="DeepSeek-R1"
)

llm_qwen3_14B = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    model="qwen/qwen3-14b:free",
    temperature=0.0,
    name="Qwen3-14B"
)

LLM_modles = [llm_llama_4_maver ,  llm_deepseek_R1,  llm_qwen3_14B]

########################################--Job Describtion--#######################################

job_desc_path = "job_descriptions.pdf"
# uploaded_resume = st.file_uploader("Upload a Resume PDF (Optional)", type='pdf')
text = extract_text_from_pdf(job_desc_path)
job_data = parse_job_descriptions(text)
job_titles = extract_job_titles(job_data)

########################################--Upload Resume--#######################################
st.header("Resume Evaluation")

def handle_pdf_input():
    """
    Handles the PDF file upload input from the user in Streamlit.
    If no file is uploaded, returns None.
    """
    uploaded_pdf = st.file_uploader("Upload your resume (PDF)", type="pdf")
    
    if uploaded_pdf is not None:
        # If the user uploaded a PDF, extract text from the file
        resume_text = extract_text_from_pdf(uploaded_pdf)
        return resume_text
    
    # If no file is uploaded, return None
    return None

resume_text = handle_pdf_input()

if resume_text:
    st.success("Resume text extracted successfully!")
    st.subheader("Resume Evaluation Results:")
    evaluate_resume_against_jobs(resume_text, job_data, job_titles, LLM_modles)
else:
    st.warning("No resume uploaded. Please upload a PDF file to proceed.")




