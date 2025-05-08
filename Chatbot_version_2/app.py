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

st.markdown("---")
st.markdown("Optionally upload a Job Description (PDF) to get a tailored analysis.")

jd_file = st.file_uploader("Upload job description (PDF)", type=["pdf"], key="jd")

jd_text = None
if jd_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_jd:
        tmp_jd.write(jd_file.read())
        jd_path = tmp_jd.name

    # Extract JD text
    jd_text = extract_text_from_pdf(jd_path)
    os.remove(jd_path)

    


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

        if jd_text:
            st.subheader("📄 Job Description Summary")
            st.text_area("Extracted Job Description", jd_text, height=200)

        # Analyze button
        if st.button("🔍 Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                result = analyze_resume(resume_text, jd_text)  

            try:
                parsed = json.loads(result)
                # st.success("✅ Analysis complete!")

                # st.subheader("💼 Suggested Job Titles")
                # for title in parsed.get("job_titles", []):
                #     st.markdown(f"- {title}")

                # st.subheader("📊 Resume Score")
                # st.markdown(f"**{parsed.get('score', 'N/A')} / 100**")

                # st.subheader("🛠️ Suggestions to Improve")
                # for suggestion in parsed.get("suggestions", []):
                #     st.markdown(f"- {suggestion}")

                # Save result to chat history
                save_message(USER_ID, "user", "Analyze Resume")

                pretty_response = (
                    f"💼 **Suggested Job Titles:**\n" +
                    "\n".join([f"- {t}" for t in parsed.get("job_titles", [])]) + "\n\n" +
                    f"📊 **Resume Score:** **{parsed.get('score', 'N/A')} / 100**\n\n" +
                    "🛠️ **Suggestions to Improve:**\n" +
                    "\n".join([f"- {s}" for s in parsed.get("suggestions", [])])
                )

                save_message(USER_ID, "assistant", pretty_response)


            except json.JSONDecodeError:
                st.error("⚠️ Failed to parse the response. Please try again.")
                st.text(result)


# Resume-related Q&A
st.divider()
st.subheader("💬 Chat with the HR Bot")


# # Show chat history
history = get_chat_history(USER_ID, limit=None)
for role, message in history:
    with st.chat_message(role):
        st.markdown(message)

# Clear chat history button
if 'confirm_delete' not in st.session_state:
    st.session_state.confirm_delete = False

if st.button("🗑️ Clear All Chat History"):
    st.session_state.confirm_delete = True

if st.session_state.confirm_delete:
    st.warning("Are you sure you want to delete all chat history? This cannot be undone.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, delete all history"):
            clear_chat_history(USER_ID)
            st.refresh()
    with col2:
        if st.button("Cancel"):
            st.session_state.confirm_delete = False

# New user message
if user_question := st.chat_input("Ask anything about your resume..."):
    # Save and show user message
    save_message(USER_ID, "user", user_question)
    with st.chat_message("user"):
        st.markdown(user_question)

    # Prepare full chat + new message for LLM
    past = get_chat_history(USER_ID)
    messages = [{"role": role, "content": msg} for role, msg in past]
    messages.append({"role": "user", "content": user_question})
    # Divider
    st.divider()
    st.subheader("⚠️ Danger Zone")
    # Clear chat history button
    if 'confirm_delete' not in st.session_state:
        st.session_state.confirm_delete = False

    if st.button("🗑️ Clear All Chat History"):
        st.session_state.confirm_delete = True

    if st.session_state.confirm_delete:
        st.warning("Are you sure you want to delete all chat history? This cannot be undone.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, delete all history"):
                clear_chat_history(USER_ID)
                st.refresh()
        with col2:
            if st.button("Cancel"):
                st.session_state.confirm_delete = False
    
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
        

        


