# nodes/logger.py
import json
from pathlib import Path
from datetime import datetime
from typing_extensions import TypedDict

LOG_PATH = Path(__file__).parents[1] / 'logs' / 'debate.log'
LOG_PATH.parent.mkdir(exist_ok=True)

def file_logger(state: TypedDict):
    """
    Append the latest round info and full state snapshot to the log file,
    then route back to validator so the loop continues until judge.
    """
    # Safeguard: write a concise per-round log entry
    last_entry = state.get('transcript', [])[-1] if state.get('transcript') else None
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.utcnow().isoformat()}] Round {state.get('round')} update\n")
        if last_entry:
            f.write(json.dumps(last_entry, ensure_ascii=False) + "\n")
        f.write("STATE SNAPSHOT:\n")
        f.write(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        f.write("---\n")

    # Continue to validator
    return {"_next": "validator"}
