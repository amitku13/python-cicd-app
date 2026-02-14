from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("ENVIRONMENT", "local")
    return f"Hello from {env} environment!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)