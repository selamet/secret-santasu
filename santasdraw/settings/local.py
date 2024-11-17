from santasdraw.settings.base import BASE_DIR

SECRET_KEY = 'django-insecure-hv70-g(368l@ls_^$h%g2k=b7om59%@x3hez(g24qo^u=0d=3g'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
