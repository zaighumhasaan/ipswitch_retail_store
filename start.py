#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}", flush=True)
    print(f"{description}", flush=True)
    print(f"{'='*50}", flush=True)
    sys.stdout.flush()
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Warning: {description} failed with code {result.returncode}", flush=True)
    sys.stdout.flush()
    return result.returncode

if __name__ == "__main__":
    print("Starting Ipswich Retail application...", flush=True)
    sys.stdout.flush()

    # Collect static files
    run_command(
        "python manage.py collectstatic --noinput",
        "Collecting static files"
    )

    # Run migrations
    run_command(
        "python manage.py migrate --noinput",
        "Running database migrations"
    )

    # Create sample data
    run_command(
        "python manage.py create_sample_data",
        "Creating sample data"
    )

    # Create default superuser if it doesn't exist
    print("\n" + "="*50, flush=True)
    print("Creating default superuser (if needed)", flush=True)
    print("="*50, flush=True)
    sys.stdout.flush()

    create_superuser_cmd = """
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@ipswich.com', 'admin123');
    print('Superuser created: username=admin, password=admin123');
else:
    print('Superuser already exists');
"""

    subprocess.run(["python", "manage.py", "shell", "-c", create_superuser_cmd])

    # Get port from environment
    port = os.environ.get('PORT', '8000')

    print(f"\n{'='*50}", flush=True)
    print(f"Starting Gunicorn on 0.0.0.0:{port}", flush=True)
    print(f"{'='*50}\n", flush=True)
    sys.stdout.flush()

    # Start Gunicorn - use subprocess instead of exec to see errors
    gunicorn_cmd = [
        "gunicorn",
        "--bind", f"0.0.0.0:{port}",
        "--workers", "3",
        "--timeout", "120",
        "--log-level", "info",
        "--access-logfile", "-",
        "--error-logfile", "-",
        "ipswich_retail.wsgi:application"
    ]

    print(f"Executing: {' '.join(gunicorn_cmd)}", flush=True)
    sys.stdout.flush()

    try:
        result = subprocess.run(gunicorn_cmd)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"ERROR starting Gunicorn: {e}", flush=True)
        sys.exit(1)
