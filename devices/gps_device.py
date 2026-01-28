from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/gps")
def gps():
    data = {
        "lat": round(48.0 + random.uniform(-0.01, 0.01), 6),
        "lon": round(2.0 + random.uniform(-0.01, 0.01), 6),
        "timestamp": time.time()
    }
    return jsonify(data)

app.run(host="0.0.0.0", port=5001)