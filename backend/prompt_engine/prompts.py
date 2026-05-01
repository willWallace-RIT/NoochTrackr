def build_prompt(state):
    return {
        "season": state.get("season", "spring"),
        "inventory": state.get("inventory", []),
        "difficulty": state.get("tier", 1)
    }
