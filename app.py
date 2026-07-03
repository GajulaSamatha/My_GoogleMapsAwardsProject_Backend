import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Initialize the .env loader before accessing any os.environ variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Pulling securely from the .env file
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST")

def get_fallback_rates():
    # Executes if the API fails, times out, or quota is exceeded
    return {"petrol": 109.52, "diesel": 95.76, "source": "fallback_static"}

@app.route('/fuel-price/<city>', methods=['GET'])
def get_fuel_price(city):
    if not RAPIDAPI_KEY or not RAPIDAPI_HOST:
        print("Server Error: Missing credentials in .env file.")
        return jsonify(get_fallback_rates()), 200

    # You MUST replace 'city_price_endpoint' with the actual endpoint from the documentation
    # that accepts a city name and returns the price.
    URL = f"https://{RAPIDAPI_HOST}/city_price_endpoint/"
    
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }

    # Pass the city as a query parameter (adjust key 'city' based on API docs)
    querystring = {"city": city}

    try:
        response = requests.get(URL, headers=headers, params=querystring, timeout=5)
        
        # Handle API quota limits or server errors gracefully
        if response.status_code in [429, 403, 500]:
            print(f"API Error {response.status_code}. Using fallback data.")
            return jsonify(get_fallback_rates()), 200
            
        response.raise_for_status()
        data = response.json()
        
        # NOTE: You will need to adjust 'data.get(...)' based on the exact JSON 
        # structure returned by this specific RapidAPI provider.
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