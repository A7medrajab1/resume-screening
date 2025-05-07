# app.py

import streamlit as st
import tempfile
import os
import json
from resume_parser import extract_text_from_pdf
from resume_analyzer import analyze_resume
from chat_memory import init_db, save_message, get_chat_history, clear_chat_history
import requests
# Initialize DB
init_db()

# Simulated user ID (can use login system later)
USER_ID = "demo_user"

st.set_page_config(page_title="HR Resume Chatbot", layout="centered")
st.title("📄 HR Resume Chatbot")
st.markdown("Upload your resume (PDF) to get job suggestions, a score, and tips!")

# Handle file upload
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract resume text
    resume_text = extract_text_from_pdf(tmp_path)
    os.remove(tmp_path)

    if resume_text:
        st.subheader("📋 Resume Summary")
        st.text_area("Extracted Resume Text", resume_text, height=300)

        # Analyze with LLM
        with st.spinner("Analyzing your resume..."):
            result = analyze_resume(resume_text)

        try:
            parsed = json.loads(result)
            st.success("✅ Analysis complete!")

            st.subheader("💼 Suggested Job Titles")
            for title in parsed.get("job_titles", []):
                st.markdown(f"- {title}")

            st.subheader("📊 Resume Score")
            st.markdown(f"**{parsed.get('score', 'N/A')} / 100**")

            st.subheader("🛠️ Suggestions to Improve")
            for suggestion in parsed.get("suggestions", []):
                st.markdown(f"- {suggestion}")

            # Save result to chat history
            save_message(USER_ID, "user", "[Uploaded Resume]")
            save_message(USER_ID, "assistant", result)

        except json.JSONDecodeError:
            st.error("⚠️ Failed to parse the response. Please try again.")
            st.text(result)

# Resume-related Q&A
# st.divider()
# st.subheader("💬 Chat with the HR Bot")

# # Show chat history
# history = get_chat_history(USER_ID, limit=10)
# for role, message in history:
#     with st.chat_message(role):
#         st.markdown(message)

# New user message
if user_question := st.chat_input("Ask anything about your resume..."):
    # 1. Save and display the user's message first
    save_message(USER_ID, "user", user_question)

    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_question)

    # 2. Construct chat history as LLM context (including the new user question)
    past = get_chat_history(USER_ID, limit=10)
    messages = [{"role": role, "content": msg} for role, msg in past]
    messages.append({"role": "user", "content": user_question})
    
    # 3. Call LLM with memory
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek/deepseek-prover-v2:free",
        "messages": messages,
        "temperature": 0.0,
    }

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload)
            )
            res.raise_for_status()
            
            # Get the response content from JSON and format it
            data = res.json()
            message_content = data["choices"][0]["message"]["content"]
            content = message_content

        except Exception as e:
            content = f"Error: {e}"

        # ✅ Always show the assistant's message whether success or error
        with st.chat_message("assistant"):
            st.markdown(content)

        # ✅ Save the assistant's message
        save_message(USER_ID, "assistant", content)

