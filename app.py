import os
import streamlit as st
import google.generativeai as genai

# Get API key from environment variable (set in GitHub Secrets)
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

st.sidebar.title("KiroHub")
page = st.sidebar.selectbox("Navigate", ["Productivity", "Play", "Learn", "Wildcard"])

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
