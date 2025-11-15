#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"{description}")
    print(f"{'='*50}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Warning: {description} failed with code {result.returncode}")
    return result.returncode

if __name__ == "__main__":
    print("Starting Ipswich Retail application...")

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

    # Get port from environment
    port = os.environ.get('PORT', '8000')

    print(f"\n{'='*50}")
    print(f"Starting Gunicorn on 0.0.0.0:{port}")
    print(f"{'='*50}\n")

    # Start Gunicorn
    gunicorn_cmd = [
        "gunicorn",
        "--bind", f"0.0.0.0:{port}",
        "--workers", "3",
        "--timeout", "120",
        "--log-level", "debug",
        "--access-logfile", "-",
        "--error-logfile", "-",
        "ipswich_retail.wsgi:application"
    ]

    os.execvp("gunicorn", gunicorn_cmd)
