![4D7A823A-1BB1-4A3C-ABB1-9660C2B3CC5D](https://github.com/user-attachments/assets/04d49b67-d94f-48df-a0d3-1ad736dc80d4)# 💼 Resume Screening System  
**Final Project – DEPI Internship | Banque Misr**

A smart, AI-powered resume screening application that leverages **Natural Language Processing (NLP)** and **Large Language Models (LLMs)** to automate and optimize the hiring process. Built to help HR professionals efficiently filter and evaluate resumes based on job requirements.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Contributors](#-contributors)

---

## 📄 Overview

Recruitment is often slowed down by manual resume screening. This project introduces a smart resume screening system that uses **NLP**, **LLMs**, and **data analysis** techniques to evaluate resumes by extracting key information like skills, experience, and education. It automatically compares resumes to job descriptions and provides feedback on candidate-job fit.

This project was developed as part of our **DEPI Internship in collaboration with Banque Misr**, showcasing the potential of **AI in HR tech**.

---

## 🛠️ Tech Stack

### 🧠 Artificial Intelligence
- **Natural Language Processing (NLP)**:
  - Tokenization, Named Entity Recognition (NER), Part-of-Speech tagging
  - Used to extract structured data from unstructured resumes
- **Large Language Models (LLMs)** (optional/future-ready):
  - Models like **GPT-3.5/4 via OpenAI API** for feedback generation
  - Used for semantic comparison between resumes and job descriptions
- **Text Similarity & Semantic Matching**:
  - TF-IDF Vectorization
  - Cosine Similarity for comparing candidate content to job criteria

### 📚 Python Libraries
| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `spaCy`       | NLP pipeline for skill/experience extraction |
| `nltk`        | Tokenization and preprocessing               |
| `PyPDF2`      | Extracting resume text from PDF files        |
| `pandas`      | Data manipulation and analysis               |
| `scikit-learn`| TF-IDF vectorization, similarity matching    |
| `openai`      | Integration with GPT-3.5/4 (optional)        |
| `streamlit`   | (optional) for interactive UI                |

---

## ✨ Features

- ✅ Extracts skills, experience, education, and keywords from resumes
- ✅ Compares resumes against job descriptions using NLP
- ✅ Ranks candidates based on job relevance
- ✅ Provides **human-readable feedback** via GPT (optional)
- ✅ Modular and easy to extend for new features
- ✅ Prepares the system for chatbot integration (future)

---

## 🧱 System Architecture

```
PDF Resumes
   |
   |--[PyPDF2]--> Extracted Text
   |
   |--[spaCy/NLTK]--> Cleaned & Tokenized Text
   |
   |--[TF-IDF Vectorizer]--> Feature Vector
   |
   |--[Cosine Similarity]--> Match Score vs Job Description
   |
   |--[LLM / GPT (Optional)]--> Feedback Generation
   |
   |--> HR Review Output
```

---

## ⚙️ Installation

1. **Clone the Repository**  
```
git clone https://github.com/A7medrajab1/resume-screening.git
cd resume-screening/Chatbot_version_1
```

2. **Create a Virtual Environment (Recommended)**  
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Dependencies**  
```
pip install -r ../requirements.txt
```

> **Note**: For GPT functionality, set up your API key from [OpenAI](https://platform.openai.com) in a `.env` or config file.

---

## ▶️ Usage

Run the main script for resume analysis:

```
python resume_analyzer.py
```

Place sample resumes inside the `/sample_resumes` folder before running.

---

## 🧪 Sample Output

```
Candidate: John Doe
Match Score: 83.7%
Extracted Skills: Python, SQL, Data Analysis, Communication
Feedback:
✔️ This candidate demonstrates solid technical background with 2+ years of experience in data analytics and a degree in computer science. Likely to be a strong match for data analyst roles.
```

---

## 🖼️ Screenshots

| Chatbot Resume Upload | Login & Register | Matching Results & Feedback |
|----------------------|------------------|----------------------------|
| ![Chatbot Upload](https://github.com/user-attachments/assets/c4532bfc-34d5-4c41-bcb3-c2455cc307b9) <br> The chatbot interface allows users to upload their resume files for screening. | ![Login/Register](https://github.com/user-attachments/assets/c17361f0-42aa-4d7f-affc-d83c09df2648) <br> Simple and secure login and registration forms for candidate access. | ![Matching Results & Feedback](https://github.com/user-attachments/assets/43b68cda-e28b-40cf-90e0-5c3ea979488f) <br> View AI-generated matching results with job descriptions and get real-time feedback on how well the resume matches the position. |


---

## 🔮 Future Improvements

- Build a **chatbot assistant** using OpenAI or LangChain for interactive Q&A
- Add a **Streamlit-based web dashboard** for HR teams
- Improve language support (Arabic/French resumes)
- Deploy as a REST API (using FastAPI or Flask)
- Store analyzed resumes in a searchable **MongoDB** or **PostgreSQL** database
- Add OCR for scanned resumes (via Tesseract)

---

## 👩‍💻 Contributors

- **Malak Mohamed** – [GitHub](https://github.com/MalakMohameed)
- **Ahmed Rajab** – [GitHub](https://github.com/A7medrajab1)
- **Remon Raafat** - [GitHub](https://github.com/remoraafat)

---

## 🏢 Developed For

This project was built as part of the **Digital Egypt Pioneers Initiative (DEPI)** and **Banque Misr Internship Program**, focusing on solving real-world HR problems using Artificial Intelligence and modern software engineering practices.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
