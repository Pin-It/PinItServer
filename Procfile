release: python pinit/manage.py migrate
web: gunicorn --log-file - --chdir pinit pinit.wsgi
