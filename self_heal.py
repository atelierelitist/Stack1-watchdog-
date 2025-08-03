# self_heal.py – Sovereign Auto-Recovery Protocol

import os
import psutil
import time
import logging

logging.basicConfig(
    filename="diagnostics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

WATCHED_PROCESS = "heartbeat.py"  # Can be changed to any script

def is_process_running(name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if name in proc.info['cmdline']:
            return True
    return False

def restart_process():
    logging.warning("🛠️ Watchdog triggered: Restarting process.")
    os.system(f"nohup python3 {WATCHED_PROCESS} &")

while True:
    if not is_process_running(WATCHED_PROCESS):
        logging.error(f"💥 {WATCHED_PROCESS} stopped unexpectedly!")
        restart_process()
    time.sleep(10)
