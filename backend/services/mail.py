from flask import render_template
from flask_mail import Message

from backend import mail
from backend.settings import settings
from backend import celery


def get_mail_template(data):
    if data[0].get("lang", "TR").lower() == settings.TR:
        return settings.TR_MAIL_TEMPLATE, settings.TR_BODY
    return settings.EN_MAIL_TEMPLATE, settings.EN_BODY


class MailService:
    def __init__(self):
        self.sender = settings.MAIL_USERNAME

    @staticmethod
    @celery.task
    def send_mail(data):
        template, body = get_mail_template(data)
        msg = Message(body, sender=settings.MAIL_USERNAME, recipients=[data[0].get('email', {})])

        msg.body = render_template(template, data=data)
        msg.html = msg.body
        mail.send(msg)

        return True
