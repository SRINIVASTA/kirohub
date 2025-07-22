import streamlit as st
import google.generativeai as genai
from utils.resume_helper import build_resume_prompt
import os

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
if not GOOGLE_API_KEY:
    st.error("Google API Key not found! Please add it to Streamlit secrets.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

st.title("🔧 Resume Helper (Gemini)")
st.markdown("Optimize your resume for a job description using Google's Gemini AI.")

resume = st.text_area("Paste your Resume here:", height=300)
job_desc = st.text_area("Paste Job Description here:", height=300)

if st.button("🛠️ Improve Resume"):
    if not resume or not job_desc:
        st.warning("Please enter both resume and job description.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            try:
                prompt = build_resume_prompt(resume, job_desc)
                response = model.generate_content(prompt)
                st.success("Suggestions ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error from Gemini: {e}")
