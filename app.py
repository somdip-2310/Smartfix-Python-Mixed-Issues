from flask import Flask, jsonify
import numpy as np
import pandas as pd
from api.routes import register_routes
from helpers import format_response

app = Flask(__name__)
register_routes(app)

@app.route("/")
def index():
    arr = np.array([10, 20, 30])
    return jsonify(format_response({"sum": int(arr.sum())}))

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
