from .base import *

SECRET_KEY = 'django-insecure-nlm)52sqdglo9b8ae#$q7g1909c8i*1*w+4$-pe5=%gkg@=%e)'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
ALLOWED_HOSTS = ['*']



