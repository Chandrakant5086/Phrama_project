import time
import os

LOG_DIR = "log_info"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Ensure folder exists
os.makedirs(LOG_DIR, exist_ok=True)

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {message}\n")
