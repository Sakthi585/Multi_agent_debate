import os
from graphviz import Digraph

def draw_graph(output_path="dag/debate_diagram.dot"):
    """
    Generates a Graphviz DAG diagram for the Multi-Agent Debate system.
    Saves both .dot and .png versions.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create the DAG using Graphviz
    dot = Digraph(comment="Multi-Agent Debate DAG", format="png")

    # Define nodes
    dot.node("UserInput", "🧑‍💻 User Input Node\n(Accepts topic)")
    dot.node("Scientist", "🔬 Agent A: Scientist\n(Argues for regulation)")
    dot.node("Philosopher", "🧠 Agent B: Philosopher\n(Argues against regulation)")
    dot.node("Memory", "💾 Memory Node\n(Stores structured summary)")
    dot.node("Judge", "⚖️ Judge Node\n(Reviews debate & declares winner)")

    # Define edges
    dot.edges([
        ("UserInput", "Scientist"),
        ("Scientist", "Memory"),
        ("Memory", "Philosopher"),
        ("Philosopher", "Memory"),
        ("Memory", "Scientist"),
        ("Memory", "Judge")
    ])

    # Save the diagram as .dot and .png
    dot.save(output_path)
    dot.render(output_path.replace(".dot", ""), format="png", cleanup=True)

    print(f"✅ DAG diagram generated at: {output_path}")
    print(f"🖼️ PNG version saved as: {output_path.replace('.dot', '.png')}")
