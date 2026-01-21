# Weather Dashboard

Full-stack project built with Django (templates) for user authentication and a personalized weather dashboard.

## Features (planned / in progress)
- User registration, login, logout
- Personalized dashboard
- Weather search by city
- External weather API integration
- Search history per user
- Automated tests (Django unittest)
- Deployment on Render (PostgreSQL)

## Tech stack
- Django
- Django Templates (no React)
- SQLite (local) / PostgreSQL (production)
- GitHub + feature branches

## Local setup
1) Create and activate virtualenv
2) Install dependencies
3) Run migrations
4) Start server

Example commands:
- `python manage.py migrate`
- `python manage.py runserver`

## Environment variables
Create a `.env` file (not committed) for secrets (API keys, etc.).  
(To be added when we integrate the weather API.)

## Tests
Run:
- `python manage.py test`

## Deployment
Planned: Render + PostgreSQL
