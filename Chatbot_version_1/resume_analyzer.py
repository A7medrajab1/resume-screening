# resume_analyzer.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from resume_parser import extract_text_from_pdf

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# MODEL = "deepseek/deepseek-prover-v2:free"
MODEL = "qwen/qwen3-1.7b:free"

def analyze_resume(resume_text):
    prompt = f"""
You are a professional HR recruiter. You are reviewing a resume provided below.
Your task is to:
1. Suggest 1–3 suitable job titles for the candidate.
2. Score the resume from 0 to 100 based on quality, clarity, and relevance.
3. Provide 3–5 specific suggestions to improve the resume.

Resume:
\"\"\"
{resume_text}
\"\"\"

Respond in this JSON format only:

{{
    "job_titles": [ ... ],
    "score": ...,
    "suggestions": [ ... ]
}}

don't include any other text in your response.
without (```json) or (```).
"""

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.0
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("test.pdf")
    result = analyze_resume(resume_text)
    print(result)