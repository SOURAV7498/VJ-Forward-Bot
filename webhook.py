from flask import Flask
import os
import subprocess
import threading
import time

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def health_check(path):
    return "VJ Forward Bot Live! 🚀"

def run_bot_background():
    """NON-BLOCKING bot start"""
    subprocess.Popen(
        ["python", "main.py"],
        stdout=open("bot.log", "a"),
        stderr=open("bot_error.log", "a"),
        start_new_session=True  # Prevents SIGTERM kill
    )
    print("🚀 Bot started in background!")

# Start bot IMMEDIATELY (NON-BLOCKING)
run_bot_background()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
