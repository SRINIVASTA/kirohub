# pages/learn_page.py

import streamlit as st
import google.generativeai as genai
import os
from utils.tutor import build_tutor_prompt

def run_learn():
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
    if not GOOGLE_API_KEY:
        st.error("Google API key not found. Please set it in Streamlit secrets or environment variables.")
        return

    genai.configure(api_key=GOOGLE_API_KEY)

    st.title("📚 AI Tutor")
    query = st.text_area("Ask me anything! Programming, science, history, etc.", height=150)

    if st.button("Get Answer"):
        if not query.strip():
            st.warning("Please enter a question or topic.")
        else:
            prompt = build_tutor_prompt(query)
            model = genai.GenerativeModel("gemini-pro")
            try:
                response = model.generate_content(prompt)
                st.markdown("### Answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"AI Error: {e}")
