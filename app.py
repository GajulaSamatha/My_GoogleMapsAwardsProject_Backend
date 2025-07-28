from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/fuel-price/<city>', methods=['GET'])
def get_fuel_price(city):
    print(f"📍 Simulating fuel price for: {city}")

    sample_data = {
        "petrol": 109.52,
        "diesel": 95.76
    }

    return jsonify(sample_data)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

