from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

EXPORT_FOLDER = "exports"

if not os.path.exists(EXPORT_FOLDER):
    os.makedirs(EXPORT_FOLDER)

@app.route("/madden/export", methods=["POST"])
def madden_export():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{EXPORT_FOLDER}/nfl_export_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    return jsonify({"status": "Export received"}), 200


@app.route("/")
def home():
    return "ÑFL Madden Export API is running 🏈"


if __name__ == "__main__":
    app.run()
