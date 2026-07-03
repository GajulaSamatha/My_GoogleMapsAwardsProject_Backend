import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Environment variables for security
FUEL_API_KEY = os.environ.get("RAPIDAPI_KEY")
FUEL_API_URL = "https://fuel-prices-in-india-api-url.p.rapidapi.com/prices"

def get_fallback_rates():
    # This executes only if the API fails or limits are exceeded
    return {"petrol": 109.52, "diesel": 95.76, "source": "fallback_static"}

@app.route('/fuel-price/<city>', methods=['GET'])
def get_fuel_price(city):
    # If API key isn't set, default to fallback immediately
    if not FUEL_API_KEY:
        return jsonify(get_fallback_rates()), 200

    headers = {
        "X-RapidAPI-Key": FUEL_API_KEY,
        "X-RapidAPI-Host": "your-chosen-api-host.p.rapidapi.com"
    }
    
    try:
        response = requests.get(f"{FUEL_API_URL}?city={city}", headers=headers, timeout=5)
        
        # Handle API quota exceeded (429) or server errors (500)
        if response.status_code in [429, 403, 500]:
            print(f"API Error {response.status_code}. Using fallback data.")
            return jsonify(get_fallback_rates()), 200
            
        # Automatically raises an exception for any other 4xx or 5xx errors
        response.raise_for_status()
        data = response.json()
        
        return jsonify({
            "petrol": data.get("petrol", 109.52),
            "diesel": data.get("diesel", 95.76),
            "source": "live_api"
        }), 200

    except requests.exceptions.RequestException as e:
        # Catches timeouts or general network failures
        print(f"Network error: {e}")
        return jsonify(get_fallback_rates()), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)