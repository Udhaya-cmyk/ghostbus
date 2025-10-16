from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

# Path to CSV
CSV_FILE = os.path.join(os.path.dirname(__file__), "delhi_buses.csv")

@app.route("/buses")
def get_buses():
    buses = []
    try:
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                buses.append({
                    "vehicle_id": row["vehicle_id"],
                    "route_id": row["route_id"],
                    "lat": float(row["lat"]),
                    "lon": float(row["lon"]),
                    "ghost_score": float(row["ghost_score"])
                })
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404
    return jsonify(buses)

if __name__ == "__main__":
    app.run(debug=True)
