def build_tutor_prompt(question: str) -> str:
    return f"""
You are a helpful and knowledgeable tutor.

Question:
{question}

Provide a clear, concise, and educational answer with examples if applicable.
"""
