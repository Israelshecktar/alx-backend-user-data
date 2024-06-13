#!/usr/bin/env python3
"""Basic falsk app"""

from flask import Flask, Request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Return a JSON paylaod with a welcome message"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")