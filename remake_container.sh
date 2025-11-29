#!/bin/sh
docker compose down
docker compose build
docker compose up -d
docker compose exec backend uv run python manage.py migrate
docker compose exec backend uv run manage.py createsuperuser --noinput
