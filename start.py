#!/usr/bin/env python
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}", flush=True)
    print(f"{description}", flush=True)
    print(f"{'='*50}", flush=True)
    sys.stdout.flush()
    
    # For database commands, retry a few times if they fail
    max_retries = 3
    for attempt in range(max_retries):
        result = subprocess.run(command, shell=True)
        if result.returncode == 0:
            return 0
        
        if "migrate" in command or "database" in description.lower():
            print(f"Attempt {attempt + 1} failed. Waiting 3 seconds before retry...", flush=True)
            time.sleep(3)
        else:
            break
    
    if result.returncode != 0:
        print(f"Warning: {description} failed with code {result.returncode}", flush=True)
    
    sys.stdout.flush()
    return result.returncode

if __name__ == "__main__":
    print("=" * 60, flush=True)
    print("Starting Ipswich Retail application on Render...", flush=True)
    print("=" * 60, flush=True)
    sys.stdout.flush()

    # Print environment info for debugging
    print(f"PORT: {os.environ.get('PORT', 'Not set')}", flush=True)
    print(f"RENDER_EXTERNAL_HOSTNAME: {os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'Not set')}", flush=True)
    print(f"DATABASE_URL: {'Set' if os.environ.get('DATABASE_URL') else 'Not set'}", flush=True)

    # Collect static files
    run_command(
        "python manage.py collectstatic --noinput",
        "Collecting static files"
    )

    # Run migrations (with retries for database connection)
    run_command(
        "python manage.py migrate --noinput",
        "Running database migrations"
    )

    # Create sample data (optional - comment out if not needed)
    # run_command(
    #     "python manage.py create_sample_data",
    #     "Creating sample data"
    # )

    # Create default superuser if it doesn't exist
    print("\n" + "="*50, flush=True)
    print("Creating default superuser (if needed)", flush=True)
    print("="*50, flush=True)
    sys.stdout.flush()

    create_superuser_cmd = """
from django.contrib.auth import get_user_model;
import os
User = get_user_model();
admin_username = os.environ.get('ADMIN_USERNAME', 'admin');
admin_email = os.environ.get('ADMIN_EMAIL', 'admin@ipswich.com');
admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123');
if not User.objects.filter(username=admin_username).exists():
    User.objects.create_superuser(admin_username, admin_email, admin_password);
    print(f'Superuser created: username={admin_username}');
else:
    print('Superuser already exists');
"""

    subprocess.run(["python", "manage.py", "shell", "-c", create_superuser_cmd])

    # Get port from environment (Render sets this automatically)
    port = os.environ.get('PORT', '8000')

    print(f"\n{'='*50}", flush=True)
    print(f"Starting Gunicorn on 0.0.0.0:{port}", flush=True)
    print(f"{'='*50}\n", flush=True)
    sys.stdout.flush()

    # Start Gunicorn
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
        # Use exec to replace the process with Gunicorn (better for signals)
        os.execvp("gunicorn", gunicorn_cmd)
    except Exception as e:
        print(f"ERROR starting Gunicorn: {e}", flush=True)
        sys.exit(1)
