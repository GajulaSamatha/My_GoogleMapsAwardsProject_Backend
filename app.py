import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS

# ---------------------------------------------------------
# ENVIRONMENT CONFIGURATION
# ---------------------------------------------------------
# This try-except block makes your code environment-agnostic.
# Locally: It imports dotenv and reads your .env file.
# On Render: It fails the import gracefully, bypasses the local file, 
# and pulls the variables directly from Render's dashboard settings.
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("📍 Running locally: Loaded variables from .env file.")
except ImportError:
    print("☁️ Running in production (Render): Using system environment variables.")
# ---------------------------------------------------------

app = Flask(__name__)
CORS(app)

# Pulling securely from either the local .env or the Render dashboard
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST")

# ... (keep the rest of your get_fallback_rates and get_fuel_price functions exactly the same)