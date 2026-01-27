from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import geocode_city, fetch_current_weather, fetch_daily_forecast
from .models import SearchHistory


def weather_theme(weather_code) -> str:
    # Open-Meteo weather codes (WMO). Grupujemy w „themes”.
    try:
        code = int(weather_code)
    except (TypeError, ValueError):
        return "default"

    if code == 0:
        return "clear"
    if code in (1, 2, 3):
        return "cloudy"
    if code in (45, 48):
        return "fog"
    if code in (51, 53, 55, 56, 57):
        return "drizzle"
    if code in (61, 63, 65, 66, 67, 80, 81, 82):
        return "rain"
    if code in (71, 73, 75, 77, 85, 86):
        return "snow"
    if code in (95, 96, 99):
        return "storm"

    return "default"


# Tlo w widokach ponizej w, index() return render =>
def index(request):
    return render(request, "index.html", {
        "body_class": "bg-home",
    })


@login_required
def dashboard(request):
    city = (request.GET.get("city") or "").strip()
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    
    forecast = []
    weather = None
    location = None
    choices = []
    error = None
    theme = "default"

   
           

    # Jeśli użytkownik kliknął konkretną lokalizację (mamy lat/lon) → pobieramy pogodę
    if city and lat and lon:
        try:
            latitude = float(lat)
            longitude = float(lon)
            weather = fetch_current_weather(latitude, longitude)

            theme = weather_theme(weather.get("weather_code"))
            forecast = fetch_daily_forecast(latitude, longitude)

            # zapis historii wyszukiwań
            SearchHistory.objects.create(
              user=request.user,
              query=city,
              latitude=latitude,
              longitude=longitude,
            )

       

            
            location = {
                "name": city, 
                "country": None, 
                "admin1": None, 
                "latitude": latitude, 
                "longitude": longitude
                }
        except Exception:
            error = "Weather service error. Please try again."
            theme = "default"
            forecast =[]

    # Jeśli użytkownik wpisał tylko nazwę miasta → pokazujemy listę propozycji
    elif city:
        try:
            choices = geocode_city(city)
            if not choices:
                error = "City not found. Try another name."
        except Exception:
            error = "Geocoding error. Please try again."
        
        
    history = SearchHistory.objects.filter(user=request.user)[:8]

    context = {
        "city": city,
        "location": location,
        "weather": weather,
        "choices": choices,
        "error": error,
        "theme": theme,
        "forecast": forecast,
        "history": history,
        "theme": theme,
        "body_class": f"theme-{theme}",
    }
    return render(request, "weather/dashboard.html", context)
