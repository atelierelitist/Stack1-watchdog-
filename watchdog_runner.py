import time
import yaml
import json
from heartbeat import check_process
from self_heal import attempt_recovery

with open("trigger_map.yaml") as f:
    triggers = yaml.safe_load(f)

with open("diagnostics.json", "r") as dfile:
    diagnostics = json.load(dfile)

def run_watchdog():
    for process_name, trigger in triggers.get("processes", {}).items():
        if not check_process(process_name):
            print(f"[!] {process_name} not running. Triggering {trigger['action']}")
            diagnostics[process_name] = "DOWN"
            attempt_recovery(trigger['action'], process_name)
        else:
            diagnostics[process_name] = "UP"

    with open("diagnostics.json", "w") as dfile:
        json.dump(diagnostics, dfile, indent=4)

# Continuous loop
while True:
    run_watchdog()
    time.sleep(10)
