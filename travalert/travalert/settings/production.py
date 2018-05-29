from __future__ import absolute_import, unicode_literals

from .base import *

import os

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost']

# Sensitive settings e.g. passwords should be stored in local.py
try:
    from .local import *
except ImportError:
    pass
