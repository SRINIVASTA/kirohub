import streamlit as st
import google.generativeai as genai
import os
from utils.resume_helper import build_resume_prompt  # import your helper function

# Setup Gemini API Key
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)

st.title("🔧 Resume Helper (Gemini)")
st.markdown("Use Google's Gemini model to optimize your resume for a job description.")

resume = st.text_area("📄 Paste your Resume", height=300)
job_desc = st.text_area("📌 Paste the Job Description", height=300)

if st.button("🛠️ Improve Resume"):
    if not resume or not job_desc:
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Gemini is analyzing your resume..."):
            try:
                model = genai.GenerativeModel("gemini-2.0-flash-exp")
                prompt = build_resume_prompt(resume, job_desc)  # use utility function here
                response = model.generate_content(prompt)
                st.success("Suggestions ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error from Gemini: {e}")
