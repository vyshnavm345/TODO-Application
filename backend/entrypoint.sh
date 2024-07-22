#!/bin/sh

echo "Starting entrypoint script..."

# Apply database migrations
python manage.py makemigrations
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8000 server.wsgi:application
