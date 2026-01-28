# Weather Dashboard

Django web application with user authentication and a weather dashboard built with Django Templates.

## Features
- User registration, login, logout
- Weather dashboard (templates)
- Weather search by city
- Open-Meteo(Geocoding + Forecast)
- Background images based on weather conditions


## Tech stack
- Django
- Django Templates
- SQLite (development)
- requests (external API calls)

## Requirements
- Python 3.13+
- pip

## Local setup
1. Clone repository
2. Create and activate virtual environment
3. Install dependencies
4. Run migrations
5. Start server

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
