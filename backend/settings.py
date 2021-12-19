from os import getenv, path, urandom
from dotenv import load_dotenv


class Settings:
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

    # Flask Settings
    SECRET_KEY = getenv("SECRET_KEY", urandom(24))
    PORT = getenv("PORT", 80)
    DEBUG = getenv("DEBUG", False)
    TESTING = getenv("TESTING", False)
    ENV = getenv("ENV", "production")

    # SQLAlchemy Settings
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///" + path.join(basedir, "oyb.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    # Flask Mail Settings
    MAIL_SERVER = getenv("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = getenv("MAIL_PORT", 587)
    MAIL_USE_TLS = getenv("MAIL_USE_TLS", True)
    MAIL_USERNAME = getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD", "")

    # Celery Settings
    CELERY_BROKER_URL = getenv("CELERY_BROKER_URL", "redis://redis:6379")
    CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND", "redis://redis:6379")

    # Const
    TR = "tr"
    EN = "en"
    TR_MAIL_TEMPLATE = "tr_email_template.html"
    EN_MAIL_TEMPLATE = "en_email_template.html"
    TR_BODY = "Yeni Yıl Çekiliş Sonuçları :)"
    EN_BODY = "Secret Santa Results :)"


settings = Settings()
