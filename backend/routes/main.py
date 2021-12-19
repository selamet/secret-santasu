from json import dumps

from flask import Blueprint, request

from backend.services.mail import MailService
from backend.helpers.raffle import match_participants

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/", methods=["POST"])
def index():
    mail_service = MailService()
    if request.get_json():
        data = match_participants(request.get_json())  # TODO: add validator or serializer
        for match in data:
            mail_service.send_mail.delay(match)

    return dumps({"success": True}), 200, {"ContentType": "application/json"},
