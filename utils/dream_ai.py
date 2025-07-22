def build_dream_prompt(dream_description: str) -> str:
    return f"""
You are an expert dream interpreter.

Interpret the symbolic and emotional meaning of this dream:

Dream:
{dream_description}
"""
