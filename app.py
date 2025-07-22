import streamlit as st
import google.generativeai as genai

# Main title for the app
st.title("Kirohub AI Platform")

# Prompt for GOOGLE_API_KEY as a password
api_key = st.text_input("Please enter your GOOGLE_API_KEY:", type="password")

# Validate and configure the API key
if api_key:
    try:
        genai.configure(api_key=api_key)
        st.session_state.api_key = api_key  # Store the API key in session state
        st.success("✅ Gemini API Key is configured and ready!")

    except Exception as e:
        st.error(f"❌ Error with the API Key: {e}")

# Side navigation for different pages
st.sidebar.title("Navigate")
page = st.sidebar.selectbox("Choose a page", ["Productivity", "Play", "Learn", "Wildcard"])

# Check if the API key is provided before loading the rest of the pages
if api_key:
    # Page routing based on selected page
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

else:
    st.warning("Please enter your GOOGLE_API_KEY to continue.")
