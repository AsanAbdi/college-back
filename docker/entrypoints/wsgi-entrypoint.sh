#!/bin/sh

until cd /app
do
    echo "Waiting for server volume..."
done

until python manage.py makemigrations
do 
    echo "Waiting for db migrations"
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 1
done

python manage.py collectstatic --noinput
python manage.py compilemessages

gunicorn tamyr.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 2
