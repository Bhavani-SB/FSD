#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install the requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create a superuser if the CREATE_SUPERUSER environment variable is set to "True"
if [[ "$CREATE_SUPERUSER" == "True" ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
