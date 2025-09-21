# Fare Estimator – Backend

This repository contains the **backend code** for the **Fare Estimator** project, a web application designed to calculate fair travel fares for auto rickshaws, private cabs, and similar transportation.

The backend is hosted and fully integrated with the frontend, which is available here: [Fare Estimator Frontend](https://fareestimator.netlify.app/)

## 🛠️ Technologies Used

- **Python (Flask)** – Backend framework to handle API requests  
- **Google Maps API** – Fetch distance between two addresses  
- **Live Fuel Price API** – Fetch current fuel prices for fare calculation  

## 🚀 Functionality

The backend calculates fares based on multiple factors:

1. **Fuel Price** – Fetches the price of fuel on the current day.  
2. **Distance** – Calculates the distance between two addresses using Google Maps API.  
3. **Ride Type** – Determines if it is a share auto or private ride.  
4. **Time of Day** – Adds extra charges for late-night travel.  
5. **Driver Workload** – Adds a small extra amount for the driver’s effort.  
6. **Vehicle Mileage** – Optional input to adjust fare based on auto mileage.  
7. **Tips** – Optional input for tipping the driver.  

The backend exposes APIs that the frontend consumes to provide **real-time fare estimations**.

## 🔗 Project Structure

- `app.py` – Main Flask application handling API requests.  
- `requirements.txt` – Python dependencies for the backend.  
- Other utility modules for calculations and integrations with external APIs.  

## 📌 Purpose

This backend exists to **support the frontend static website** by providing accurate, real-time fare calculations based on multiple parameters. This allows users to estimate fares transparently and fairly.

## 📬 Contact

For inquiries or feedback, please reach out via [your email](mailto:samathagajulaofficial@gmail.com).

---

Frontend link: [Fare Estimator Frontend](https://fareestimator.netlify.app/)
