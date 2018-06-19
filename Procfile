release: python manage.py migrate; python manage.py loaddata auth
web: bin/start-nginx gunicorn -c gunicorn.conf --enable-stdio-inheritance --log-file - pinit.wsgi
