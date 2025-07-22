import streamlit as st

# Main title for the app
st.title("Kirohub AI Platform")

# Side navigation for different pages
st.sidebar.title("Navigate")
page = st.sidebar.selectbox("Choose a page", ["Productivity", "Play", "Learn", "Wildcard"])

# Ask for the Google API Key if it is not already in session_state
if 'google_api_key' not in st.session_state:
    st.session_state.google_api_key = st.text_input("Enter your Google API Key", type="password")
    if st.session_state.google_api_key:
        st.session_state.api_key_provided = True
    else:
        st.session_state.api_key_provided = False

# Ensure the API key is provided before showing any content
if not st.session_state.api_key_provided:
    st.warning("Please enter the Google API Key to proceed.")
else:
    # Page routing
    if page == "Productivity":
        from pages.1_Productivity import run_productivity
        run_productivity(st.session_state.google_api_key)

    elif page == "Play":
        from pages.2_Play import run_play
        run_play(st.session_state.google_api_key)

    elif page == "Learn":
        from pages.3_Learn import run_learn
        run_learn(st.session_state.google_api_key)

    elif page == "Wildcard":
        from pages.4_Wildcard import run_wildcard
        run_wildcard(st.session_state.google_api_key)
