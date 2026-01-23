import requests


def geocode_city(city: str) -> dict | None:
    """
    Zamienia nazwę miasta na współrzędne (lat/lon) używając Open-Meteo Geocoding API.
    Zwraca dict z lat/lon/name/country albo None jeśli brak wyników.
    """
    city = (city or "").strip()
    if not city:
        return None

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    results = data.get("results") or []
    if not results:
        return None

    item = results[0]
    return {
        "name": item.get("name"),
        "country": item.get("country"),
        "latitude": item.get("latitude"),
        "longitude": item.get("longitude"),
    }


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    """
    Pobiera aktualną pogodę (temperatura, wiatr) z Open-Meteo Forecast API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    current = data.get("current") or {}
    return {
        "temperature_2m": current.get("temperature_2m"),
        "wind_speed_10m": current.get("wind_speed_10m"),
        "time": current.get("time"),
    }
