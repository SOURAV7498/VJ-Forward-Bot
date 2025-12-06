from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def health_check(path):
    return "VJ Forward Bot ULTRA FAST! ⚡"

# ULTRA FAST BOT START (NO UVLOOP needed)
subprocess.Popen([
    "python", "main.py",
    "--fast-mode",
    "--no-db-logs"
], stdout=open("bot.log", "a"), 
stderr=open("bot_error.log", "a"),
start_new_session=True)
print("⚡ ULTRA FAST Bot started! (No uvloop)")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
