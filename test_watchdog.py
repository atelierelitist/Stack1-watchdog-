import subprocess
import time

# Simulated process
def start_dummy_process():
    return subprocess.Popen(["sleep", "9999"])

def kill_process(proc):
    proc.terminate()

if __name__ == "__main__":
    print("[+] Starting dummy process...")
    proc = start_dummy_process()
    time.sleep(5)

    print("[!] Killing process to trigger watchdog...")
    kill_process(proc)

    # Wait to allow watchdog to detect
    print("[*] Waiting for watchdog to react...")
    time.sleep(15)

    print("[✓] Test complete.")
