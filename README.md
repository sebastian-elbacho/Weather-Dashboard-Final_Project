# Weather Dashboard / UCD Assignment (31.01.2026)
## Live Demo
https://weather-dashboard-final-project.onrender.com


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



## Environment Variables

### Local Development
- DJANGO_SECRET_KEY
- DJANGO_DEBUG=True
- DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

### Production (Render)
- DJANGO_SECRET_KEY
- DJANGO_DEBUG=False
- DJANGO_ALLOWED_HOSTS=weather-dashboard-final-project.onrender.com
- CSRF_TRUSTED_ORIGINS=https://weather-dashboard-final-project.onrender.com
- DATABASE_URL (Render PostgreSQL)


## Deployment (Render)

The application is deployed using Render Web Service and PostgreSQL.

### Build Command
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

### Start Command
gunicorn config.wsgi:application


## Static Files

Static files (CSS, images, background JPGs) are served in production using WhiteNoise.


## Hosting Compatibility

The application is fully compatible with Render hosting requirements and uses
environment variables, Gunicorn, PostgreSQL, and WhiteNoise for production deployment.
