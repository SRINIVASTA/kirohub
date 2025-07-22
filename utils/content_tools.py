# kirohub/utils/content_tools.py

def rewrite_content(content: str, tone: str) -> str:
    """
    Create a prompt for rewriting content in a given tone.
    """
    return (
        f"Rewrite the following content in a {tone} tone:\n\n"
        f"{content}\n\n"
        "Ensure it remains clear and engaging."
    )
