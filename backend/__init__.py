from flask import Flask
from flask_mail import Mail
from flask_cors import CORS

from celery import Celery
from backend.settings import settings

mail = Mail()
cors = CORS()
celery = Celery(__name__, broker=settings.CELERY_BROKER_URL)


def init_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    mail.init_app(app)
    cors.init_app(app)
    init_celery(app)

    from backend.routes.main import main
    app.register_blueprint(main)  # urlprefix = "/"

    return app
