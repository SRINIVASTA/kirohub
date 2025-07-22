# pages/productivity_page.py

import streamlit as st
import google.generativeai as genai
from utils.resume_helper import build_resume_prompt

def run_productivity():
    st.title("📄 Resume Optimizer for Job Matching")

    resume_text = st.text_area("Paste your resume here:", height=200)
    job_description = st.text_area("Paste the job description here:", height=200)

    if st.button("Get AI Suggestions"):
        if not resume_text.strip() or not job_description.strip():
            st.warning("Please provide both resume and job description.")
            return

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = build_resume_prompt(resume_text, job_description)

            with st.spinner("Analyzing your resume..."):
                response = model.generate_content(prompt)

            st.subheader("💡 Suggestions to Improve Your Resume:")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Error generating content: {e}")
