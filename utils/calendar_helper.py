# kirohub/utils/calendar_helper.py

def summarize_schedule(schedule_text: str) -> str:
    """
    Create a prompt to summarize and prioritize tasks from a schedule.
    """
    return (
        f"Here is a schedule or task list:\n\n{schedule_text}\n\n"
        "Summarize the key tasks, remove duplication, and prioritize the items clearly."
    )
