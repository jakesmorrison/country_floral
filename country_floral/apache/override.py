#override.py

from jakobmorrison.settings import *

DEBUG = False
ALLOWED_HOSTS = ['www.countryfloralidaho.com','countryfloralidaho.com', '192.241.213.57']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/root/database/db.sqlite3",
    }
}

