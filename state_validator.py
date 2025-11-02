def validate_state(state: dict) -> None:
    """
    Validate the current debate state to ensure all required keys exist.
    Prevents runtime errors due to missing or malformed state entries.
    """
    required_keys = ["topic", "round", "agent_turn", "transcript"]
    for key in required_keys:
        if key not in state:
            raise ValueError(f"Missing required key in state: '{key}'")

    if not isinstance(state["transcript"], list):
        raise TypeError("State field 'transcript' must be a list.")

    if not isinstance(state["round"], int) or state["round"] < 1:
        raise ValueError("State field 'round' must be a positive integer.")
