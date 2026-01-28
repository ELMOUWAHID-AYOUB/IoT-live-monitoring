from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/battery")
def battery():
    data = {
        "battery": random.randint(50, 100)
    }
    return jsonify(data)

app.run(host="0.0.0.0", port=5002)
