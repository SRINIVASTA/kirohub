import sys
import pathlib

# Ensure the project root is in Python's module search path
sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()))

import os
import streamlit as st
import google.generativeai as genai

# Configure Google API key
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

# Sidebar navigation for KiroHub
st.sidebar.title("KiroHub")
page = st.sidebar.selectbox("Navigate", ["Productivity", "Play", "Learn", "Wildcard"])

try:
    if page == "Productivity":
        from pages.productivity_page import run_productivity
        run_productivity()

    elif page == "Play":
        from pages.play_page import run_play
        run_play()

    elif page == "Learn":
        from pages.learn_page import run_learn
        run_learn()

    elif page == "Wildcard":
        from pages.wildcard_page import run_wildcard
        run_wildcard()
except Exception as e:
    st.error(f"Failed to load `{page}` page: {e}")
