from __future__ import absolute_import, unicode_literals

import django_heroku

from .base import *

import os

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['pin-it-app.herokuapp.com']

django_heroku.settings(locals())

