#!/bin/sh

if [ "$DB_USER" = "postgres" ]; then
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
fi

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"
