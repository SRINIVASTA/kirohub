import streamlit as st
from google import genai
from utils.resume_helper import build_resume_prompt  # your helper function

st.set_page_config(page_title="Resume Helper (Gemini)", layout="wide")
st.title("🔧 Resume Helper (Google Gemini)")

st.markdown("""
Use Google's Gemini model to optimize your resume for a job description.

⚠️ **Please enter your Google API key below to proceed.**
""")

# Ask user for API key interactively
api_key = st.text_input("🔐 Enter your Google API Key", type="password")
if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

# Initialize client
try:
    client = genai.Client(api_key=api_key)
    model = client.models.get("gemini-2.0-flash-exp")  # or your preferred model name
except Exception as e:
    st.error(f"❌ Failed to initialize Google Gemini client: {e}")
    st.stop()

# Get resume and job description from user
resume = st.text_area("📄 Paste your Resume", height=300)
job_desc = st.text_area("📌 Paste the Job Description", height=300)

if st.button("🛠️ Improve Resume"):
    if not resume.strip() or not job_desc.strip():
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Gemini is analyzing your resume..."):
            try:
                prompt = build_resume_prompt(resume, job_desc)
                response = model.generate_content(prompt)
                st.success("Suggestions ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error from Gemini: {e}")
