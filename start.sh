#!/bin/bash
set -e

echo "Starting Django application..."

echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "Static files collection failed, continuing..."

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Creating superuser if needed..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" || echo "Superuser creation skipped"

echo "Starting Gunicorn server on port ${PORT:-8000}..."
exec gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 3 --timeout 120 --log-level info --access-logfile - --error-logfile - ipswich_retail.wsgi:application
