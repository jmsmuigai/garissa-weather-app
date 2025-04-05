import requests
from django.shortcuts import render

def home(request):
    api_key = "272673e2a3ef998211ae5c4c86845e3f"  # Your API key
    city = "Garissa"  # Default city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        weather_data = response.json()

        context = {
            "city": city,
            "temperature": weather_data.get("main", {}).get("temp"),
            "description": weather_data.get("weather", [{}])[0].get("description"),
            "icon": weather_data.get("weather", [{}])[0].get("icon"),
        }
    except requests.exceptions.RequestException:
        context = {
            "city": city,
            "temperature": "N/A",
            "description": "Unable to fetch weather data",
            "icon": None,
        }

    return render(request, "home.html", context)

"""
Garissa Weather App

This is a Django-based weather application that fetches real-time weather data for Garissa using the OpenWeatherMap API.

Features:
- Displays current temperature, weather description, and an icon.
- Fetches data from OpenWeatherMap API.
- Includes a map of Garissa.

Requirements:
- Python 3.9 or higher
- Django 4.2.20
- Requests library

Installation:
1. Clone the repository:
   git clone https://github.com/jmsmuigai/garissa-weather-app.git
   cd garissa-weather-app

Push the `README.md` to GitHub:
1. Add the `README.md` file to Git:
   git add README.md
   git commit -m "Add comprehensive README.md"
"""

# Dependencies
# Django==4.2.20
# requests==2.31.0
