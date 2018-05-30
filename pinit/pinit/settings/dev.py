from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qd1#yo1&-nhw8rw$sh2@xa5(p8i(l^e!4p)7emcqmtiuw2+j+o'

ALLOWED_HOSTS = ['*']

# Sensitive settings e.g. passwords should be stored in local.py
try:
    from .local import *
except ImportError:
    pass
