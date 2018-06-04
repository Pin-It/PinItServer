release: python manage.py migrate; python manage.py loaddata auth
web: gunicorn --log-file - pinit.wsgi
