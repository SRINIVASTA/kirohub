import streamlit as st
import google.generativeai as genai
import os

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)

st.title("🃏 Wildcard Fun")

mode = st.radio("Choose your fun:", ["Dream Interpreter", "Chat with Historical Figure"])

if mode == "Dream Interpreter":
    dream = st.text_area("Describe your dream:", height=200)
    if st.button("Interpret Dream"):
        if not dream.strip():
            st.warning("Please describe your dream.")
        else:
            prompt = f"""
You are an expert dream interpreter.

Given this dream description, provide a symbolic and emotional interpretation:

Dream:
{dream}
"""
            model = genai.GenerativeModel("gemini-pro")
            try:
                response = model.generate_content(prompt)
                st.markdown("### Interpretation:")
                st.write(response.text)
            except Exception as e:
                st.error(f"AI Error: {e}")

elif mode == "Chat with Historical Figure":
    figure = st.selectbox("Pick a figure to chat with:", ["Albert Einstein", "Marie Curie", "Martin Luther King Jr.", "Ada Lovelace"])
    question = st.text_area(f"Ask {figure} anything:", height=150)
    if st.button("Chat"):
        if not question.strip():
            st.warning("Please enter your question.")
        else:
            prompt = f"""
You are impersonating {figure}, responding in their style and knowledge.

Question:
{question}

Answer as {figure} would.
"""
            model = genai.GenerativeModel("gemini-pro")
            try:
                response = model.generate_content(prompt)
                st.markdown(f"### {figure} says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"AI Error: {e}")
