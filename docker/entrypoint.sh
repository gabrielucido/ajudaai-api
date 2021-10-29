#!/bin/sh

echo "Apply database migrations"
python manage.py migrate --fake-initial

if [ "$ENVIRONMENT" != "production" ]
then
    echo "Loading Fixtures..."
    python manage.py loaddata project/fixtures/*.json
fi

python manage.py runserver 0.0.0.0:9000
