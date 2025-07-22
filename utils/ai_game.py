def build_game_prompt(current_story: str, player_action: str) -> str:
    return f"""
You are the narrator of a text adventure game.

Current story:
{current_story}

Player action:
{player_action}

Continue the story in a vivid, engaging way with consequences and new options.
"""
