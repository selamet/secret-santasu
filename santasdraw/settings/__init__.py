from decouple import config

from santasdraw.settings.base import *

if config('ENVIRONMENT') == 'production':
    from santasdraw.settings.production import *
elif config('ENVIRONMENT') == 'staging':
    from santasdraw.settings.staging import *
else:
    from santasdraw.settings.local import *
