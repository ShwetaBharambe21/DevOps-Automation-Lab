from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter("request_count", "Total Request Count")


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return """
    <h1>🚀 DevOps Automation Lab</h1>
    <h3>Version 3</h3>
    <p>Successfully running inside Docker.</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)