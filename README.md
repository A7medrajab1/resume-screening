# Resume Screening App  
This project represents our **Final Bank Misr Internship Project**. It is a machine learning-based resume screening system that streamlines the hiring process by automatically analyzing and evaluating resumes.

## Overview  
The Resume Screening project is designed to reduce the time and effort spent by HR teams during the candidate selection process. It uses natural language processing (NLP) and machine learning to assess resumes based on job descriptions and required qualifications.

The system flags qualified candidates and generates feedback in a human-readable format to support decision-making.

The main logic of the application resides in the [`resume_analyzer.py`](https://github.com/A7medrajab1/resume-screening/blob/main/Chatbot_version_1/resume_analyzer.py) file located in the `Chatbot_version_1` directory.

## Features

This system includes several core features:
- **Resume Parsing:** Extracts relevant content from PDF and text resumes.
- **Job Matching:** Compares candidate qualifications with job descriptions.
- **Skills Extraction:** Identifies and highlights technical and soft skills.
- **Feedback Generation:** Produces concise feedback indicating match level.
- **Interactive Chatbot Integration:** Future-ready for chatbot interaction for real-time screening.

## Prerequisites

Before running the code, ensure the following are installed:
- Python 3.7 or later
- Required Python packages:
  - `pandas`
  - `spacy`
  - `PyPDF2`
  - `sklearn`
  - `nltk`
  - `streamlit` *(deployment)*

Install dependencies using:
```

pip install -r requirements.txt

```

## Steps to Run

1. **Clone the repository**:
```

git clone [https://github.com/A7medrajab1/resume-screening.git](https://github.com/A7medrajab1/resume-screening.git)

```

2. **Navigate to the project directory**:
```

cd resume-screening/Chatbot\_version\_1

```

3. **Run the resume analyzer script**:
```

python resume\_analyzer.py

```

> *Make sure to modify any API keys or paths if needed before execution.*

## Architecture  
The project uses a **Modular Script-Based Architecture**:
- ___Data Ingestion___: Reads resumes from local storage.
- ___Text Preprocessing___: Cleans, tokenizes, and processes text using NLP tools.
- ___Matching Algorithm___: Compares extracted skills/experience with job description.
- ___Feedback Engine___: Outputs human-readable analysis or scores.

## Directory Structure

```

resume-screening/
├── Chatbot\_version\_1/
│   ├── resume\_analyzer.py     # Main script for resume screening
│   ├── utils.py               # Helper functions (optional)
│   └── sample\_resumes/        # Folder containing test resume files
├── README.md
└── requirements.txt           # Python dependencies

```

## Sample Output

- Matched Score: 87%
- Extracted Skills: Python, SQL, Machine Learning, Communication
- Feedback:
  > *“This candidate has strong programming skills and relevant experience in data analysis. Consider shortlisting.”*

## Future Enhancements
- Streamlit-based UI for HR teams.
- Integration with chatbots for real-time interaction.
- Support for multiple job role screening.
- Dashboard for visual analytics.

## Resources
- Refer to the core analyzer script [here](https://github.com/A7medrajab1/resume-screening/blob/main/Chatbot_version_1/resume_analyzer.py).

## Contributors
- Malak Mohamed - [GitHub](https://github.com/MalakMohameed)  
- Ahmed Rajab - [GitHub](https://github.com/A7medrajab1)
- Remon Raafat - [GitHub](https://github.com/remoraafat)

# HR Resume Chatbot
The HR Resume Chatbot is an AI-powered web application designed to help job seekers optimize their resumes for better job opportunities. Users can upload their resume and optionally a job description in PDF format. The app analyzes the resume, provides a score, suggests relevant job titles, and offers actionable tips for improvement. It also includes a chatbot feature that allows users to interactively ask questions about their resume. The system supports user registration and login, stores personalized chat history, and leverages large language models to deliver accurate feedback, all within a user-friendly Streamlit interface.