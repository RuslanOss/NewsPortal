FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONWRITEBYTECODE=1 PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=NewsPaper.settings
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput || true
EXPOSE 8000
CMD ["gunicorn", "NewsPaper.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
