from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "NFLxTwisterPFF API running"

# Endpoint comodín para Madden
@app.route("/madden/export/<path:subpath>", methods=["POST"])
def madden_export(subpath):
    data = request.get_json(silent=True)

    print("=== MADDEN EXPORT ===")
    print("PATH:", subpath)
    print("DATA:", data)

    return jsonify({
        "status": "ok",
        "path": subpath
    }), 200


if __name__ == "__main__":
    app.run()
