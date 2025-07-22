import streamlit as st
import google.generativeai as genai
import os
from utils.ai_game import build_game_prompt

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)

st.title("🎮 Mini AI Text Adventure")

if "story" not in st.session_state:
    st.session_state.story = "You find yourself in a mysterious forest. What do you do?"
    st.session_state.history = []

st.markdown(f"**Story so far:** {st.session_state.story}")

choice = st.text_input("What do you do next? (Type your action)")

if st.button("Continue Adventure"):
    if choice.strip() == "":
        st.warning("Please enter your action!")
    else:
        prompt = build_game_prompt(st.session_state.story, choice)
        model = genai.GenerativeModel("gemini-pro")
        try:
            response = model.generate_content(prompt)
            st.session_state.history.append(choice)
            st.session_state.story = response.text.strip()
            st.experimental_rerun()
        except Exception as e:
            st.error(f"AI Error: {e}")
