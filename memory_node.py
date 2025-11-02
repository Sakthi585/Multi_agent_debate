# nodes/memory_node.py
from typing_extensions import TypedDict

def memory_node(state: TypedDict):
    """
    Update per-agent short summaries and a short-term memory (last 4 lines).
    Provide only relevant memory for the next agent (not full state sharing).
    """
    # Build per-agent short summary: keep the last 2 arguments for each agent
    summaries = state.get('summaries', {'Scientist': [], 'Philosopher': []})
    for agent in ('Scientist', 'Philosopher'):
        last = state.get('last_arguments', {}).get(agent, [])[-2:]
        summaries.setdefault(agent, []).append(' | '.join(last) if last else '')

    # Short-term memory: last 4 transcript lines
    transcript = state.get('transcript', [])
    short_memory = transcript[-4:]

    # Store updates in state
    state['summaries'] = summaries
    state['short_memory'] = short_memory

    # Next: logger
    return {"_next": "logger", "summaries": summaries, "short_memory": short_memory}
