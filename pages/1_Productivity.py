import streamlit as st
from google import genai
from utils.resume_helper import build_resume_prompt

import streamlit as st

def run_productivity():
    st.header("Welcome to the Productivity Page!")
    # Add more content for the Productivity page here


# Get API key from user input
api_key = st.text_input("Enter your Google API Key", type="password")
if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

# Initialize client
client = genai.Client(api_key=api_key)

# Inputs
resume = st.text_area("Paste your Resume", height=300)
job_desc = st.text_area("Paste the Job Description", height=300)

if st.button("Improve Resume"):
    if not resume.strip() or not job_desc.strip():
        st.warning("Please provide both resume and job description.")
    else:
        prompt = build_resume_prompt(resume, job_desc)
        with st.spinner("Gemini is analyzing your resume..."):
            try:
                # Directly generate content
                response = client.generate_content(
                    model="gemini-2.0-flash-exp",
                    prompt=prompt,
                )
                # The generated text is usually in response.candidates[0].content
                st.markdown(response.candidates[0].content)
            except Exception as e:
                st.error(f"Error from Gemini: {e}")
