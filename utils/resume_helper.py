# kirohub/utils/resume_helper.py

def build_resume_prompt(resume_text: str, job_description: str) -> str:
    """
    Build a prompt for the AI to suggest improvements or tailoring
    of a resume based on the given job description.

    Args:
        resume_text (str): The user's resume content.
        job_description (str): The job description to tailor for.

    Returns:
        str: A formatted prompt string for the AI.
    """
    prompt = (
        f"Given the following resume:\n{resume_text}\n\n"
        f"And the following job description:\n{job_description}\n\n"
        "Provide suggestions on how to improve or tailor the resume "
        "to better match the job description. Include keywords, skills, "
        "and phrasing recommendations."
    )
    return prompt
