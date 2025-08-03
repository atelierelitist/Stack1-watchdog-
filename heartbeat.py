import time
import json
import os
from datetime import datetime

# Define the critical service you want to monitor
WATCHED_PROCESS = "self_heal.py"
DIAG_FILE = "diagnostics.json"

def log_issue(reason):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "issue": reason
    }
    if os.path.exists(DIAG_FILE):
        with open(DIAG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(entry)
    with open(DIAG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def is_alive():
    try:
        # Check if the file is still accessible or simulate a health check
        return os.path.exists(WATCHED_PROCESS)
    except Exception as e:
        log_issue(f"Error checking health: {str(e)}")
        return False

def main():
    while True:
        if not is_alive():
            log_issue("Heartbeat failed: self_heal.py not found or unresponsive")
            os.system("python3 self_heal.py")  # Trigger healing
        time.sleep(10)  # Run check every 10 seconds

if __name__ == "__main__":
    main()
