"""
URL configuration for garissa_weather project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Route for the home view
    path('', include('weather_data.urls')),  # Include weather_data app URLs
]

# home.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Garissa Weather</title>
</head>
<body>
    <h1>🌤️ Garissa Weather</h1>
    <p><strong>City:</strong> {{ city }}</p>
    <p><strong>Temperature:</strong> {{ temperature }}°C</p>
    <p><strong>Description:</strong> {{ description }}</p>
    {% if icon %}
        <img src="http://openweathermap.org/img/wn/{{ icon }}@2x.png" alt="Weather Icon">
    {% endif %}
</body>
</html>
"""
