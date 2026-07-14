from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 DevOps Automation Lab</h1>
    <h3>Version 2</h3>
    <p>Successfully running inside Docker.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)