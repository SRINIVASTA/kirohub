# utils/resume_helper.py

def build_resume_prompt(resume_text: str, job_desc: str) -> str:
    return f"""
Act as a resume optimization expert.

Given the following RESUME and JOB DESCRIPTION, provide:
1. Tailored suggestions to align the resume to the role
2. Rewritten or improved bullet points
3. Skills or experience that should be added

Resume:
{resume_text}

Job Description:
{job_desc}
"""
