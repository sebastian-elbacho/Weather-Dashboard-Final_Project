from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import geocode_city, fetch_current_weather


def index(request):
    return render(request, "index.html")


@login_required
def dashboard(request):
    city = (request.GET.get("city") or "").strip()

    weather = None
    location = None
    error = None

    if city:
        try:
            location = geocode_city(city)
            if not location:
                error = "City not found. Try another name."
            else:
                weather = fetch_current_weather(location["latitude"], location["longitude"])
        except Exception:
            error = f"Weather service error: {e}"

    context = {
        "city": city,
        "location": location,
        "weather": weather,
        "error": error,
    }
    return render(request, "weather/dashboard.html", context)
