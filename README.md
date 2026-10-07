# NewsPortal

Modern news portal built with Django 4.2 + DRF + Apple-style design.

## Stack
- **Backend:** Django 4.2, DRF, django-allauth, dj-rest-auth
- **Database:** PostgreSQL 15
- **Frontend:** HTML5, CSS3 (Apple-style), JS, Font Awesome 6
- **Infra:** Docker, Nginx, Gunicorn, WhiteNoise
- **Docs:** drf-yasg (Swagger/ReDoc)

## Quick Start
```bash
git clone https://github.com/RuslanOss/NewsPortal.git
cd NewsPortal
cp .env.example .env
docker compose up -d --build
```

## API Endpoints
- `GET /api/posts/` — list posts
- `GET /api/posts/{id}/` — post detail
- `POST /api/posts/` — create (admin)
- `GET /api/categories/` — list categories
- `GET /api/comments/` — list comments
- `POST /api/auth/login/` — login
- `POST /api/auth/registration/` — register

Swagger: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/
