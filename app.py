from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h1>SWE40006 Task 4.2 - Credit</h1>"
        "<p>Hello from my Docker Flask application.</p>"
        f"<p>Container hostname: {socket.gethostname()}</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))