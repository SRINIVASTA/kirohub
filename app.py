import streamlit as st

# Main title for the app
st.title("Kirohub AI Platform")

# Side navigation for different pages
st.sidebar.title("Navigate")
page = st.sidebar.selectbox("Choose a page", ["Productivity", "Play", "Learn", "Wildcard"])

# Page routing based on selected page
if page == "Productivity":
    from pages.1_Productivity import run_productivity
    run_productivity()

elif page == "Play":
    from pages.2_Play import run_play
    run_play()

elif page == "Learn":
    from pages.3_Learn import run_learn
    run_learn()

elif page == "Wildcard":
    from pages.4_Wildcard import run_wildcard
    run_wildcard()
