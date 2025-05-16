# Streamlit Chat Application

A conversational AI application powered by OpenRouter API with chat history persistence.

## Installation

### Prerequisites
- Python 3.11.11
- Conda (recommended) or pip
- OpenRouter API key

### Environment Setup

#### Using Conda (recommended)

```bash
conda create -n chat_app python=3.11.11
conda activate chat_app


### Using Python venv

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


### Package Installation
pip install -r requirements.txt

### Add your OpenRouter API key in .env file:
OPENROUTER_API_KEY=your_api_key_here

### Running the Application:
streamlit run app.py