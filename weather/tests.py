

# Create your tests here.
from django.test import TestCase
from unittest.mock import patch, Mock

from .services import geocode_city, fetch_current_weather, fetch_daily_forecast


class WeatherServicesTests(TestCase):
    def test_geocode_city_empty_returns_empty_list(self):
        self.assertEqual(geocode_city(""), [])
        self.assertEqual(geocode_city(None), [])

    @patch("weather.services.requests.get")
    def test_fetch_current_weather_returns_expected_keys(self, mock_get):
        # mock response from requests.get().json()
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "current": {
                "temperature_2m": 10.5,
                "apparent_temperature": 9.0,
                "relative_humidity_2m": 55,
                "wind_speed_10m": 3.2,
                "is_day": 1,
                "time": "2026-01-28T12:00",
                "weather_code": 3,
            }
        }
        mock_get.return_value = mock_response

        data = fetch_current_weather(52.52, 13.405)

        self.assertIn("temperature_2m", data)
        self.assertIn("apparent_temperature", data)
        self.assertIn("relative_humidity_2m", data)
        self.assertIn("wind_speed_10m", data)
        self.assertIn("is_day", data)
        self.assertIn("time", data)
        self.assertIn("weather_code", data)

    @patch("weather.services.requests.get")
    def test_fetch_daily_forecast_builds_list(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "daily": {
                "time": ["2026-01-28", "2026-01-29", "2026-01-30", "2026-01-31", "2026-02-01"],
                "temperature_2m_max": [10, 11, 12, 13, 14],
                "temperature_2m_min": [2, 3, 4, 5, 6],
                "precipitation_sum": [0, 1, 0, 2, 0],
            }
        }
        mock_get.return_value = mock_response

        forecast = fetch_daily_forecast(52.52, 13.405)

        self.assertEqual(len(forecast), 5)
        self.assertEqual(forecast[0]["date"], "2026-01-28")
        self.assertIn("tmax", forecast[0])
        self.assertIn("tmin", forecast[0])
        self.assertIn("rain", forecast[0])




# TEST dashboard(u) =>

from django.urls import reverse
from django.contrib.auth import get_user_model


class WeatherViewsTests(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 302)

    def test_dashboard_renders_for_logged_in_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/dashboard.html")
