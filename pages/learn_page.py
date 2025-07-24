import streamlit as st
import google.generativeai as genai
import os
from utils.tutor import build_tutor_prompt

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)

st.title("📚 AI Tutor")

query = st.text_area("Ask me anything! Programming, science, history, etc.", height=150)

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question or topic.")
    else:
        prompt = f"""
You are a helpful and knowledgeable tutor.

Question:
{query}

Please provide a clear, concise, and educational answer, including examples or explanations if relevant.
"""
        model = genai.GenerativeModel("gemini-pro")
        try:
            response = model.generate_content(prompt)
            st.markdown("### Answer:")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
