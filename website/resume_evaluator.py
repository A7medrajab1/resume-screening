import json
from langchain import LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st


# your existing prompts

job_title_prompt = PromptTemplate(
    input_variables=["resume_text" , "job_Titles"],
    template="""
You are an AI recruiter. Based on the following resume text, identify the most appropriate job title this resume fits:

Resume:
{resume_text}

Job Titles:
{job_Titles}

Return only the job title.
"""
)


resume_match_prompt = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
You are a talent evaluator. Based on the resume and job description below, evaluate how well this resume matches the job description. 

Resume:
{resume_text}

Job Description:
{job_description}

Return a score from 0 to 100 indicating the match accuracy (100 = perfect match, 0 = no match).
Also, provide a one-sentence justification for your score.

Format:
Score: <number>
Reason: <short explanation>
"""
)

def build_job_description_text(job_dict):
    return f"""
Job Title: {job_dict["Job_Title"]}
Job Summary: {job_dict["Job_Summary"]}
Key Responsibilities: {job_dict["Key_Responsibilities"]}
Qualifications: {job_dict["Qualifications"]}
Skills: {job_dict["Skills"]}
"""

def evaluate_resume_against_jobs(resume_text, job_data, job_titles, models):
    st.markdown("---")
    st.subheader("🔍 Evaluation Results")
    
    for model in models:
        with st.container():
            st.markdown(f"### Model: `{model.get_name()}`")

            # Predict job title using the model
            job_title_chain = LLMChain(llm=model, prompt=job_title_prompt)
            predicted_title = job_title_chain.run({
                "resume_text": resume_text,
                "job_Titles": ", ".join(job_titles)
            }).strip()

            st.write(f"**Predicted Job Title:** {predicted_title}")

            # Find matching job description
            matching_job = next((job for job in job_data if job["Job_Title"].lower() == predicted_title.lower()), None)

            if not matching_job:
                st.error("❌ No matching job title found in job data.")
                continue

            # Build job description text
            job_description_full = build_job_description_text(matching_job)

            # Evaluate the match between the resume and job description
            match_chain = LLMChain(llm=model, prompt=resume_match_prompt)
            result = match_chain.run({
                "resume_text": resume_text,
                "job_description": job_description_full
            })

            st.success("✅ Match Evaluation Result:")
            st.markdown(f"```\n{result.strip()}\n```")
            st.markdown("---")



