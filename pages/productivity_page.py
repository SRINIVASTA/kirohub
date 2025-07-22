import streamlit as st
import google.generativeai as genai

def run_productivity():
    st.title("Productivity Enhancer")

    # Get the API key from the session state (already set in the main app)
    api_key = st.session_state.get("api_key", None)

    if api_key:
        # Allow user input for their task or productivity query
        user_query = st.text_area("Enter your productivity-related task or query:")

        if user_query:
            try:
                # Generate a response from the Gemini model
                prompt = f"Provide productivity-enhancing suggestions for the following task: {user_query}"
                response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)

                # Display the AI-generated response
                st.subheader("AI Suggestions:")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error generating content: {e}")
        else:
            st.warning("Please enter a query to get suggestions.")
    else:
        st.warning("API Key is not configured. Please enter it in the main app.")

