import fitz
import io
import re

def extract_text_from_pdf(pdf_file):
    """
    Extract text from the provided PDF file.
    Accepts either a file path or a file-like object.
    """
    if isinstance(pdf_file, str):  # If it's a file path
        doc = fitz.open(pdf_file)
    else:  # If it's a file-like object (uploaded PDF)
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text


def parse_job_descriptions(text):
    job_splits = re.split(r'\n\d+\.\s+', text.strip())[0:]  # Split on numbered jobs
    jobs = []

    for job_text in job_splits:
        job_title = re.search(r'Job Title:\s*(.+)', job_text)
        summary = re.search(r'Job Summary:\s*(.+?)(?=Key Responsibilities:)', job_text, re.DOTALL)
        responsibilities = re.search(r'Key Responsibilities:\s*(.+?)(?=Qualifications:)', job_text, re.DOTALL)
        qualifications = re.search(r'Qualifications:\s*(.+?)(?=Skills:)', job_text, re.DOTALL)
        skills = re.search(r'Skills:\s*(.+)', job_text, re.DOTALL)

        job_dict = {
            "Job_Title": job_title.group(1).strip() if job_title else None,
            "Job_Summary": summary.group(1).strip() if summary else None,
            "Key_Responsibilities": responsibilities.group(1).strip() if responsibilities else None,
            "Qualifications": qualifications.group(1).strip() if qualifications else None,
            "Skills": skills.group(1).strip() if skills else None,
        }

        jobs.append(job_dict)

    return jobs

def extract_job_titles(job_data):
    return [job["Job_Title"] for job in job_data]
