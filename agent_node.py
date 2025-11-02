# nodes/agent_node.py
from typing_extensions import TypedDict

AGENT_PERSONAS = {
    'Scientist': [
        'AI must be regulated like medicine due to safety-critical failures and reproducibility issues.',
        'Regulatory frameworks ensure standards, testing, and post-market surveillance for high-risk AI.',
        'Medical-style regulation reduces harm and provides a path for certified deployment in critical sectors.',
        'Precedent from medical device regulation demonstrates how patient safety can be prioritized.'
    ],
    'Philosopher': [
        'Regulation can stifle intellectual exploration and the open exchange of ideas.',
        'Overly-prescriptive rules may entrench existing paradigms and slow philosophical progress.',
        'Ethical reflection needs freedom; premature regulation could ossify moral positions.',
        'History shows that regulation often lags and can hinder cultural evolution.'
    ]
}

def agent_node_factory(state: TypedDict):
    """
    Agent generates one argument based on its persona and current round.
    """
    turn = state['agent_turn']
    spoken_count = len(state['last_arguments'].get(turn, []))
    idx = min(spoken_count, 3)

    argument = AGENT_PERSONAS[turn][idx] if idx < len(AGENT_PERSONAS[turn]) else f"{turn} provides a closing statement."

    # Save the argument
    state['last_arguments'].setdefault(turn, []).append(argument)

    # ✅ Store transcript entries as dicts (not strings)
    state.setdefault('transcript', []).append({
        "round": state['round'],
        "agent": turn,
        "argument": argument
    })

    print(f"{turn}: {argument}")

    # Move to memory
    return {"_next": "memory"}
