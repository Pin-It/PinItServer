release: python manage.py migrate; python manage.py loaddata auth
web: bin/start-nginx bundle exec gunicorn --log-file - pinit.wsgi
