import streamlit as st
import google.generativeai as genai

from utils.resume_helper import build_resume_prompt
from utils.dev_automation import generate_commit_and_issue
from utils.content_tools import rewrite_content
from utils.calendar_helper import summarize_schedule

def run_productivity():
    st.title("📄 Productivity & Workflow Tools")
    st.write("Welcome to the Productivity Page!")

    st.markdown("""
Build tools that save time, reduce friction, or simplify everyday tasks - for developers or anyone else.  
If it boosts your flow, it fits here. Examples: dev workflow automations, resume helpers, content tools, calendar organizers.
""")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🛠️ Resume Helper",
        "⚙️ Dev Automation",
        "📝 Content Rewriter",
        "📅 Calendar Organizer"
    ])

    # Resume Helper Tab
    with tab1:
        st.header("🛠️ Resume Helper with AI Suggestions")
        st.markdown("""
Example:

Resume:
Experienced software developer with 5 years in Python and AI.

Job Description:
Looking for a Python developer familiar with AI and ML techniques.
""")
        resume = st.text_area("Paste your resume here:", height=200)
        job = st.text_area("Paste the job description here:", height=200)

        if st.button("Get AI Suggestions"):
            if not resume.strip() or not job.strip():
                st.warning("Both fields are required.")
            else:
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = build_resume_prompt(resume, job)
                    with st.spinner("Analyzing..."):
                        response = model.generate_content(prompt)
                    st.subheader("💡 Suggestions:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

    # Dev Automation Tab
    with tab2:
        st.header("⚙️ Generate Dev Commit & GitHub Issue")
        st.markdown("""
Example:

Describe your dev task or bug:

fix bug in user login function - now handles invalid inputs better

- added check for empty username and password
- return proper error message to client
- refactored login handler for better readability
""")
        task = st.text_area("Describe your dev task or bug:", key="dev_task")
        if st.button("Generate Dev Artifacts"):
            if task.strip():
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = generate_commit_and_issue(task)
                    with st.spinner("Working..."):
                        response = model.generate_content(prompt)
                    st.subheader("🔧 Output:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter a task description.")

    # Content Rewriter Tab
    with tab3:
        st.header("📝 Rewrite Content with AI")
        st.markdown("""
Example:

Paste an email or message and choose a tone (Formal, Friendly, Persuasive).

Hi team,

please find the attached report for Q2.

thanks,
John
""")
        content = st.text_area("Paste your content (email, text, etc.):", key="content_text")
        tone = st.selectbox("Select tone", ["Formal", "Friendly", "Persuasive"], key="tone_select")
        if st.button("Rewrite Content"):
            if content.strip():
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = rewrite_content(content, tone)
                    with st.spinner("Rewriting..."):
                        response = model.generate_content(prompt)
                    st.subheader("✏️ Rewritten Content:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please paste some content.")

    # Calendar Organizer Tab
    with tab4:
        st.header("📅 Smart Schedule Organizer")
        st.markdown("""
Example:

Paste your tasks or schedule like:

Submit assignment by 25th July  
Doctor appointment on Saturday  
Buy groceries  
23rd July 2025 Job in Oracle
""")
        schedule = st.text_area("Paste your schedule, tasks, or to-dos:", key="schedule_input")
        if st.button("Summarize & Prioritize"):
            if schedule.strip():
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = summarize_schedule(schedule)
                    with st.spinner("Organizing..."):
                        response = model.generate_content(prompt)
                    st.subheader("✅ Prioritized Tasks:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please provide your schedule or task list.")
