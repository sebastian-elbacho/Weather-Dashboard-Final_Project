import requests


def geocode_city(city: str) -> list[dict]:
    city = (city or "").strip()
    if not city:
        return []

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 5, "language": "en", "format": "json"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    results = data.get("results") or []
    choices = []
    for item in results:
        choices.append({
            "name": item.get("name"),
            "country": item.get("country"),
            "admin1": item.get("admin1"),  # region/voivodeship/state (czasem jest)
            "latitude": item.get("latitude"),
            "longitude": item.get("longitude"),
        })
    return choices





def fetch_current_weather(latitude: float, longitude: float) -> dict:
    """
    Pobiera aktualną pogodę (temperatura, wiatr) z Open-Meteo Forecast API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,is_day,weather_code",

    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    current = data.get("current") or {}
    return {
    "temperature_2m": current.get("temperature_2m"),
    "apparent_temperature": current.get("apparent_temperature"),
    "relative_humidity_2m": current.get("relative_humidity_2m"),
    "wind_speed_10m": current.get("wind_speed_10m"),
    "is_day": current.get("is_day"),
    "time": current.get("time"),
    "weather_code": current.get("weather_code"),

}

