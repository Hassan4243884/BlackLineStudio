from .base import *

DEBUG = False

SECRET_KEY = '8gp%_&agl$l2(tc%9x+8t3ls(!h&f7ooe@34@pypa@qxrr(st2'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'black_line_studio',
        'USER': 'black_line_studio',
        'HOST': '10.11.29.106',
        'PASSWORD': '124AhCOtQrTp'
    }
}

ALLOWED_HOSTS = ['test86.icmconsulting.com', 'blacklinestudios.ca', 'www.blacklinestudios.ca']

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
