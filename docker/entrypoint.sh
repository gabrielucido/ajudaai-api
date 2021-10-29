#!/bin/sh

if [ "$DATABASE_SYSTEM" = "postgres" ]
then
    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
      echo "Initializing Postgres..."
      sleep 0.1
    done
    echo "Postgres Started!"
fi

echo "Apply database migrations"
python manage.py migrate --fake-initial

if [ "$ENVIRONMENT" != "production" ]
then
    echo "Loading Fixtures..."
    python manage.py loaddata project/fixtures/*.json
fi

python manage.py runserver 0.0.0.0:8000
