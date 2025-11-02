# nodes/judge_node.py
def judge_node(state):
    transcript = state.get("transcript", [])
    scientist_points = 0
    philosopher_points = 0

    for item in transcript:
        text = item['argument'].lower()
        if any(word in text for word in ["safety", "risk", "regulate", "standard"]):
            scientist_points += 1
        elif any(word in text for word in ["freedom", "autonomy", "ethic", "culture"]):
            philosopher_points += 1

    winner = "Scientist" if scientist_points >= philosopher_points else "Philosopher"

    summary = (
        f"Scientist focused on structured, risk-based reasoning; "
        f"Philosopher emphasized ethics and autonomy."
    )

    reason = f"{winner} provided more logically grounded and coherent arguments."

    print("[Judge] Summary of debate:")
    print(summary)
    print(f"[Judge] Winner: {winner}")
    print(f"Reason: {reason}")

    state['judge_summary'] = summary
    state['judge_winner'] = winner
    state['judge_reason'] = reason
    return state
