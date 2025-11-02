import os
from langgraph.graph import StateGraph, END
from utils.state_validator import validate_state
from utils.graphviz_helper import draw_graph


def agent_scientist(state):
    """Scientist's turn"""
    round_num = state["round"]

    responses = [
        "AI must be regulated due to high-risk applications.",
        "Regulations ensure AI safety and accountability.",
        "Unregulated AI could cause social and ethical harm.",
        "Without oversight, AI might surpass human control.",
        "Ethical AI frameworks protect public trust.",
        "Regulation aligns AI progress with societal needs.",
        "Unchecked AI could lead to biased or unsafe outcomes.",
        "Responsible AI governance ensures a safer future."
    ]

    if round_num <= len(responses):
        response = f"[Round {round_num}] Scientist: {responses[(round_num - 1) // 2]}"
        print(response)
        state["history"].append(response)

    # Next turn: Philosopher
    state["turn"] = "philosopher"
    state["round"] += 1
    return state


def agent_philosopher(state):
    """Philosopher's turn"""
    round_num = state["round"]

    responses = [
        "Regulation could stifle philosophical progress and autonomy.",
        "Freedom drives innovation more than control.",
        "Ethical growth emerges through open exploration.",
        "Excessive rules limit intellectual creativity.",
        "AI regulation risks enforcing rigid moral frameworks.",
        "Society evolves best when ideas are freely tested.",
        "Control often reflects fear, not reason.",
        "History shows overregulation often delays societal evolution."
    ]

    if round_num <= len(responses) * 2:
        response = f"[Round {round_num}] Philosopher: {responses[(round_num - 2) // 2]}"
        print(response)
        state["history"].append(response)

    # If final round reached → go to judge
    if round_num >= state["max_rounds"]:
        state["turn"] = "judge"
    else:
        state["turn"] = "scientist"
        state["round"] += 1

    return state


def judge_node(state):
    """Judge summarizes and declares winner"""
    print("\n[Judge] Summary of debate:\n")

    winner = "Scientist"
    reason = "Presented more grounded, risk-based arguments aligned with public safety principles."

    print(f"[Judge] Winner: {winner}")
    print(f"Reason: {reason}\n")

    with open("debate_log.txt", "w", encoding="utf-8") as f:
        for line in state["history"]:
            f.write(line + "\n")
        f.write(f"\nWinner: {winner}\nReason: {reason}\n")

    print("✅ Debate complete. Transcript saved to debate_log.txt")
    return END


def cli_run():
    print("Multi-Agent Debate DAG using LangGraph")
    topic = input("Enter topic for debate: ").strip()
    print(f"Starting debate between Scientist and Philosopher...\n")

    # Initial debate state
    state = {
        "topic": topic,
        "round": 1,
        "max_rounds": 8,
        "turn": "scientist",
        "history": []
    }

    # Define graph (for completeness)
    graph = StateGraph(dict)
    graph.add_node("scientist", agent_scientist)
    graph.add_node("philosopher", agent_philosopher)
    graph.add_node("judge", judge_node)
    graph.add_edge("scientist", "philosopher")
    graph.add_edge("philosopher", "scientist")
    graph.add_edge("philosopher", "judge")
    graph.set_entry_point("scientist")

    try:
        from utils.graphviz_helper import draw_graph
        draw_graph("dag/debate_diagram.dot")
    except Exception:
        print("⚠️ Could not render graph (not required for CLI execution).")

    # Sequential debate loop
    while True:
        if state["turn"] == "scientist":
            state = agent_scientist(state)
        elif state["turn"] == "philosopher":
            state = agent_philosopher(state)
        elif state["turn"] == "judge":
            judge_node(state)
            break
        else:
            break


if __name__ == "__main__":
    cli_run()
