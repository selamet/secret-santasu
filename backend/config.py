SECRET_KEY = "linuxdegilgnulinux"

# Flask-Mail
MAIL_SERVER = "smtp.googlemail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "email"
MAIL_PASSWORD = "password"


# Celery
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
