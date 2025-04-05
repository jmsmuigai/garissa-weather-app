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
