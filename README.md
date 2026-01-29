# Weather Dashboard / UCD Assignment (31.01.2026)

Django web application with user authentication and a personalized weather dashboard built using Django Templates.

---

## Features
- User registration, login, logout
- Personalized dashboard available after login
- Weather search by city
- Current weather and 5-day forecast
- Search history saved per user
- Dynamic UI themes based on weather conditions
- Subtle UI animations for better user experience

---

## External API
This project integrates the **Open-Meteo API**:
- Geocoding API (city → latitude / longitude)
- Forecast API (current weather and daily forecast)

The API is used to fetch real-time weather data based on user input.

---

## Tech stack
- Django
- Django Templates
- SQLite (local development)
- PostgreSQL (production – Render)
- requests (external API calls)

---

## Requirements
- Python 3.13+
- pip

---

## Local setup
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Start the development server

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
