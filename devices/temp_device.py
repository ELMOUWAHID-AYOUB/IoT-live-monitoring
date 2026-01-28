from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/temperature")
def temp():
    data = {
        "temperature": round(20 + random.uniform(-5, 5), 2)
    }
    return jsonify(data)

app.run(host="0.0.0.0", port=5003)