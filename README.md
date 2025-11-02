Multi-Agent Debate DAG using LangGraph
🔍 Project Description

This project implements a Multi-Agent Debate System using LangGraph, where two AI agents — a Scientist and a Philosopher — engage in a structured 8-round debate over a user-defined topic.
Each agent alternates turns, contributing logical arguments based on their persona.
A Memory Node maintains the conversation history, and a Judge Node evaluates the debate, summarizes the discussion, and declares the winner with justification.

⚙️ Features

✅ LangGraph DAG Workflow – Designed as a Directed Acyclic Graph with clearly defined nodes for input, agents, memory, and judgment.
✅ 8-Round Debate System – Alternating arguments between two AI agents (4 rounds each).
✅ Memory Management – Each agent accesses only relevant context through a Memory Node.
✅ State Validation – Ensures logical progression, correct turn-taking, and no repetition.
✅ Automated Judge Node – Analyzes stored debate history and provides a rational verdict.
✅ CLI Interface – Fully interactive command-line experience for entering topics and viewing debates.
✅ Logging System – All arguments, transitions, and final results are saved to a log file.
✅ DAG Diagram – Visual representation of node connections and debate flow.

🧩 Workflow Nodes

UserInputNode – Accepts debate topic from the user.

AgentA (Scientist) – Presents arguments in favor of regulation.

AgentB (Philosopher) – Presents counterarguments promoting freedom and creativity.

MemoryNode – Stores and updates structured debate history.

JudgeNode – Summarizes debate, analyzes reasoning, and declares the winner.

📁 Project Structure
multi_agent_debate/
│
├── main.py                     # Main entry point for CLI debate
├── utils/
│   ├── graphviz_helper.py      # Generates DAG diagrams
│   └── state_validator.py      # Validates agent state and debate flow
│
├── dag/
│   ├── debate_diagram.dot      # Graphviz DOT file defining DAG structure
│   └── debate_diagram.png      # Visual diagram of the LangGraph flow
│
├── logs/
│   └── debate.log              # Full transcript and judgment log
│
├── requirements.txt            # Dependencies list
└── README.md                   # Documentation

🧠 Example CLI Run
$ python main.py

Multi-Agent Debate DAG using LangGraph
Enter topic for debate: Should AI be regulated like medicine?

Starting debate between Scientist and Philosopher...

[Round 1] Scientist: AI must be regulated due to high-risk applications.
[Round 2] Philosopher: Regulation could stifle philosophical progress and autonomy.
...
[Round 8] Philosopher: History shows overregulation often delays societal evolution.

[Judge] Summary of debate:
[Judge] Winner: Scientist
Reason: Presented more grounded, risk-based arguments aligned with public safety principles.

✅ Debate complete. Transcript saved to debate_log.txt

🧾 How to Run

Clone the repository:

git clone https://github.com/<your-username>/multi_agent_debate.git
cd multi_agent_debate


Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate   # (On Windows: .venv\Scripts\activate)


Install dependencies:

pip install -r requirements.txt


Run the debate system:

python main.py
