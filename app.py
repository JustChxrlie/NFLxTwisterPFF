from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_DIR = "data/exports"
PASSING_FILE = os.path.join(DATA_DIR, "passing.json")

os.makedirs(DATA_DIR, exist_ok=True)


@app.route("/")
def home():
    return "NFLxTwisterPFF API running"


# Recibe export de Madden
@app.route("/madden/export/<path:subpath>", methods=["POST"])
def madden_export(subpath):
    data = request.get_json(silent=True)

    # EJEMPLO: detectar passing stats
    if "passing" in subpath.lower():
        with open(PASSING_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    return jsonify({"status": "ok"}), 200


# Endpoint para el frontend
@app.route("/api/stats/passing", methods=["GET"])
def get_passing_stats():
    if not os.path.exists(PASSING_FILE):
        return jsonify([])

    with open(PASSING_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data)


if __name__ == "__main__":
    app.run()
