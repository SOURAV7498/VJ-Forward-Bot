from flask import Flask
import os
import subprocess
import time

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def health_check(path):
    return "VJ Forward Bot ULTRA FAST + Media Fix! ⚡"

def run_bot_ultra_fast():
    subprocess.Popen([
        "python", "main.py",
        "--fast-mode",
        "--no-db-logs",
        "--fix-media-groups"  # NEW FLAG
    ], stdout=open("bot.log", "a"), 
    stderr=open("bot_error.log", "a"),
    start_new_session=True)
    print("⚡ ULTRA FAST Bot + Media Group Fix started!")

run_bot_ultra_fast()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
