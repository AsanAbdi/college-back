#!/bin/sh

until cd /app
do
    echo "Waiting for server volume..."
done

until python manage.py makemigrations
do 
    echo "Waiting for database to be ready for migrations..."
    sleep 2
done

until python manage.py migrate
do
    echo "Waiting for database to accept migrations..."
    sleep 2
done

python manage.py collectstatic --noinput

python manage.py compilemessages

exec gunicorn tamyr.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2
