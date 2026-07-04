import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Initialize the .env loader
load_dotenv()

app = Flask(__name__)
CORS(app)

# Secure credential loading
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST")

def get_fallback_rates():
    return {"petrol": 109.52, "diesel": 95.76, "source": "fallback_static"}

@app.route('/fuel-price/<city>', methods=['GET'])
def get_fuel_price(city):
    if not RAPIDAPI_KEY or not RAPIDAPI_HOST:
        print("Server Error: Missing credentials in .env file.")
        return jsonify(get_fallback_rates()), 200

    # 1. Corrected URL endpoint
    URL = f"https://{RAPIDAPI_HOST}/petrol_price_india_city_value/"
    
    # 2. Corrected Headers (Injecting the requested city directly into the header block)
    # Using .title() to ensure it matches format like "Chennai" instead of "chennai"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json",
        "City": city.title() 
    }

    try:
        # Note: 'params' argument is removed since it is handled in headers
        response = requests.get(URL, headers=headers, timeout=5)
        
        # Handle API quota limits or server errors gracefully
        if response.status_code in [429, 403, 500]:
            print(f"API Error {response.status_code}. Using fallback data.")
            return jsonify(get_fallback_rates()), 200
            
        response.raise_for_status()
        data = response.json()
        
        # DEBUG STEP: This prints the exact API response to your terminal
        print(f"Raw API Data Received: {data}")
        
        # 3. JSON Parsing Mapping
        # If this still returns fallback numbers, look at the terminal output from the print statement above.
        # Ensure that "petrol_price" and "diesel_price" exactly match the keys in that dictionary.
        return jsonify({
            "petrol": data.get("petrol_price", 109.52),
            "diesel": data.get("diesel_price", 95.76),
            "source": "live_api"
        }), 200

    except requests.exceptions.RequestException as e:
        print(f"Network or Timeout Error: {e}")
        return jsonify(get_fallback_rates()), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)