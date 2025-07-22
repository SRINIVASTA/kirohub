# utils/resume_helper.py

def build_resume_prompt(resume: str, job_desc: str) -> str:
    return f"""Compare the following resume with the job description and provide suggestions to improve the resume.

Resume:
{resume}

Job Description:
{job_desc}

Return your suggestions in a bullet-point format.
"""
