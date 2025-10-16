# ingester.py

from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow frontend JS to fetch data

CSV_FILE = "delhi_buses.csv"  # Make sure this file exists in same folder

@app.route("/")
def home():
    return "Bus ingester API is running. Use /buses to get data."

@app.route("/buses")
def get_buses():
    """
    Reads CSV and returns bus data in JSON format.
    Expected CSV columns: BusID,Route,Latitude,Longitude
    """
    if not os.path.exists(CSV_FILE):
        return jsonify({"error": f"{CSV_FILE} not found"}), 404

    try:
        df = pd.read_csv(CSV_FILE)
        required_cols = {"BusID", "Route", "Latitude", "Longitude"}
        if not required_cols.issubset(df.columns):
            return jsonify({"error": f"CSV must contain columns: {required_cols}"}), 400

        bus_data = df.to_dict(orient="records")
        return jsonify(bus_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
