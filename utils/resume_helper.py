def build_resume_prompt(resume_text: str, job_desc: str) -> str:
    return f"""
You are an expert career coach and recruiter.

Given the following resume and job description, suggest tailored improvements, skills to highlight, and rewrite bullet points if necessary.

Resume:
{resume_text}

Job Description:
{job_desc}
"""

