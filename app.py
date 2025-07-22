import streamlit as st

# Main title for the app
st.title("Kirohub AI Platform")

# Side navigation for different pages
st.sidebar.title("Navigate")
page = st.sidebar.selectbox("Choose a page", ["Productivity", "Play", "Learn", "Wildcard"])

# Page routing
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
