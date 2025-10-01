from flask import Flask, request, jsonify
from nasa_api import check_firms, check_gpm, check_modis

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate_site():
    data = request.get_json(force=True)
    lat = data.get("lat")
    lon = data.get("lon")

    if lat is None or lon is None:
        return jsonify({"error": "lat and lon are required"}), 400

    results = {
        "wildfire_risk": check_firms(lat, lon),
        "flood_risk": check_gpm(lat, lon),
        "land_use": check_modis(lat, lon)
    }
    return jsonify({"input": {"lat": lat, "lon": lon}, "results": results}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
