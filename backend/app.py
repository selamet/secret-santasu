from flask import Flask, request, json
from flask_mail import Mail, Message
from celery_config import make_celery

import time
import ast
import random

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]

# set up Flask-Mail Integration
mail = Mail(app)

app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379",
    CELERY_RESULT_BACKEND="redis://localhost:6379",
)
celery = make_celery(app)


# Add this decorator to our send_mail function
@celery.task(name="main.celery")
def send_mail(data):
    """Function to send emails."""
    with app.app_context():
        msg = Message("Ping!", sender="admin.ping", recipients=[data["email"]])
        msg.body = f"{ data['name'] } sen { data['friend'] } e hediye alacaksın :)"
        mail.send(msg)


@app.route("/", methods=["POST"])
def hello_world():
    email_list = []

    if request.method == "POST":
        if request.form:
            r = request.form
            for i in r:
                email_list = ast.literal_eval(i)

                for email in email_list:
                    print(
                        f"{ email['name'] }, { random.choice(email_list)['name'] } e hediye alacak."
                    )
                    email['friend'] = random.choice(email_list)['name']
                    send_mail.apply_async(args=[email])

            return (
                json.dumps({"success": True}),
                200,
                {"ContentType": "application/json"},
            )
        # elif request.args:
        #     r = request.args.to_dict()
        #     print(r)
        else:
            return (
                json.dumps({"success": False}),
                404,
                {"ContentType": "application/json"},
            )