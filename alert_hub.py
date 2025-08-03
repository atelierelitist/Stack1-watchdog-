import datetime

def send_alert(message):
    # For now, just logs locally — future: email, Telegram, Slack
    alert = f"[ALERT {datetime.datetime.now()}] {message}"
    print(alert)
    with open("diagnostics.json", "a") as log:
        log.write(alert + "\n")

# Example use
if __name__ == "__main__":
    send_alert("Simulated process failure on nginx.")
