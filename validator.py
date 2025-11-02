# nodes/validator.py
from typing_extensions import TypedDict

def validator_node(state: TypedDict):
    """
    Controls debate flow:
    - Ensures turn order alternates correctly
    - Stops after max_rounds
    - Returns _next node
    """
    # Increment round count (each validator call == 1 turn)
    current_round = state.get('round', 0)

    if current_round >= state['max_rounds']:
        print("[Judge] Debate rounds complete — moving to judgment...")
        return {"_next": "judge"}

    # Determine agent based on current round number
    next_agent = 'Scientist' if current_round % 2 == 0 else 'Philosopher'
    state['agent_turn'] = next_agent
    state['round'] = current_round + 1  # increment AFTER choosing agent

    print(f"[Round {state['round']}] {state['agent_turn']}'s turn...")

    # Avoid duplicate last arguments
    for agent, args in state.get('last_arguments', {}).items():
        if len(args) >= 2 and args[-1].strip() == args[-2].strip():
            args[-1] += " (rephrased to avoid repetition)"

    return {"_next": "agent"}
