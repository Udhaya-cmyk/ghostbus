from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from your frontend

@app.route("/buses")
def get_buses():
    """
    Reads bus data CSV and returns JSON.
    CSV must have headers: BusID,Route,Latitude,Longitude
    """
    try:
        df = pd.read_csv("delhi_buses.csv")  # Make sure the file is in same folder
        # Convert data to JSON format
        bus_data = df.to_dict(orient="records")
        return jsonify(bus_data)
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
