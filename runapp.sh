#!/bin/bash

ADMIN_NAME="admin"
ADMIN_EMAIL="admin@myproject.com"
PASSWORD="password"

python3 -m venv venv

activate () {
  . ../.venv/bin/activate
}

python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata professions.json
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
User.objects.create_superuser('$ADMIN_NAME', '$ADMIN_EMAIL', '$PASSWORD')" | python manage.py shell
python3 manage.py runserver
