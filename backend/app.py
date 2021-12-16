import random

from flask import Flask, json, render_template, request
from flask_cors import CORS
from flask_mail import Mail, Message

from celery_config import make_celery

from const import (
    TR,
    TR_BODY,
    EN_BODY,
    TR_MAIL_TEMPLATE,
    EN_MAIL_TEMPLATE
)

app = Flask(__name__)

CORS(app)

app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]


# set up Flask-Mail Integration
mail = Mail(app)

app.config.update(
    CELERY_BROKER_URL="redis://redis:6379",
    CELERY_RESULT_BACKEND="redis://redis:6379",
)
celery = make_celery(app)


# Add this decorator to our send_mail function
@celery.task(name="main.celery")
def send_mail(data):
    """Function to send emails."""
    with app.app_context():
        template, body = get_mail_template(data)
        msg = Message(body, sender="admin.ping",
                      recipients=[data[0].get('email', {})])

        msg.body = render_template(template, data=data)
        msg.html = msg.body
        mail.send(msg)


@app.route("/", methods=["POST"])
def hello_world():
    if request.method == "POST":
        if request.get_json():
            data = match_participants(request.get_json())
            for match in data:
                send_mail.apply_async(args=[match])

        return (
            json.dumps({"success": True}),
            200,
            {"ContentType": "application/json"},
        )
    else:
        return (
            json.dumps({"success": False}),
            404,
            {"ContentType": "application/json"},
        )


def match_participants(data):
    suitable = data[:]
    accept_array = []
    arr = []

    for i in data:
        min_arr = []
        min_arr.append(i)
        arr.append(min_arr)

    for index, val in enumerate(arr):
        suitable2 = suitable[:]
        suitable2.remove(val[0])

        r = random.choice([a for a in suitable2 if a not in accept_array])
        accept_array.append(r)
        val.append(r)

    return arr


def get_mail_template(data):
    if data[0]["lang"].lower() == TR:
        return TR_MAIL_TEMPLATE, TR_BODY
    return EN_MAIL_TEMPLATE, EN_BODY
