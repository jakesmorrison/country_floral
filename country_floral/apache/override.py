#override.py

from country_floral.settings import *

DEBUG = False
ALLOWED_HOSTS = ['https://www.countryfloralidaho.com','www.countryfloralidaho.com','countryfloralidaho.com', '198.199.102.149']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/root/database/db.sqlite3",
    }
}


