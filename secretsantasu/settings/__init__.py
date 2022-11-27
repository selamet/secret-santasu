from .base import *

if env("ENV_NAME") == 'production':
    from .prod import *
else:
    from .local import *
