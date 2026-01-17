@app.route("/madden/export", methods=["POST"])
@app.route("/madden/export/<path:subpath>", methods=["POST"])
def madden_export(subpath=None):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON received"}), 400

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if subpath:
            safe_path = subpath.replace("/", "_")
            filename = f"{EXPORT_FOLDER}/export_{safe_path}_{timestamp}.json"
        else:
            filename = f"{EXPORT_FOLDER}/export_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        print(f"✅ Export recibido: {filename}")

        return jsonify({"status": "Export received"}), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": "Server error"}), 500
