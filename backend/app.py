from flask import Flask, request, json
from flask_mail import Mail, Message
from celery_config import make_celery
from flask_cors import CORS, cross_origin

import time
import ast
import random

app = Flask(__name__)

CORS(app)

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
        msg = Message("Yeni Yıl Çekiliş Sonuçları :)", sender="admin.ping", recipients=[data[0].get('email', {})])
        # msg.body = f"{data[0].get('name', {})} sen {data[1].get('name', {})} e hediye alacaksın :)"

        address = ''
        if data[1].get('address', None):
            address = f"""
                    <tr>
                        <td style="text-align:center; margin-left:auto; margin-right:auto; padding-top: 20px">
                            <div style="background: #EFEFEF; padding: 10px 20px;border-radius: 4px;width: 70%;margin-left: auto;margin-right: auto;">
                                <p style="text-align:center; color:#3A4149; font-size:18px; font-weight:300; padding-top:10px">
                                    <span style="font-weight:400">Adres Bilgisi : </span> {data[1].get('address', "")}
                                </p>
                            </div>
                        </td>
                    </tr>
                    """

        msg.mod= f"""
        <table style="width:100%; margin-bottom:40px">
                <tr>
                    <td style="text-align:center; margin-left:auto; margin-right:auto; padding-top: 40px">
                        <img
                            style="width:300px;height:300px"
                            src ="https://i.hizliresim.com/2c63286.png" 
                        >
                    </td>
                </tr>
                <tr>
                    <p style="text-align:center; font-size:30px; padding-top:20px; color: rgb(221, 76, 79);">
                        Mutlu Yıllar {data[0].get('name', {})}
                    </p>
                </tr>
                <tr>
                    <p style="text-align:center; font-size:16px; font-weight:500; opacity: .8; padding-top:10px">
                        2022 yılında neşeniz, sağlığınız, mutluluğuz ve huzurunuz eksik olmasın. Mutlu yıllar dileriz.
                    </p>
                </tr>
                <tr>
                    <p style="text-align:center">
                        Hediye alacağın kişi
                    </p>
                </tr>
                <tr>
                    <td style="text-align:center; margin-left:auto; margin-right:auto; padding-top: 10px">
                        <div style="background: rgb(221, 76, 79); padding: 10px 20px;border-radius: 4px;width: 300px;margin-left: auto;margin-right: auto;">
                            <p style="text-align:center; color:white; font-size:18px; font-weight:600; padding-top:10px">
                                {data[1].get('name', {})}
                            </p>
                        </div>
                    </td>
                </tr>
                {address}
                <tr>
                    <td style="width:70%">
                        <div style="padding: 10px 20px;border-radius: 4px;width: 70%;margin-left: auto;margin-right: auto;">
                            <p style="text-align:center; font-size:14px">
                                Web sitemizi <a style="font-weight:400;" href="https://yilbasicekilisi.online/">buradan</a> ziyaret edebilir, 
                                projenin kaynak kodlarına<a style="font-weight:400;" href="https://github.com/selamet/online-yilbasi-cekilisi"> 
                                bu bağlantı</a> üzerinden ulaşabilirsiniz. Bize de hediye almak isterseniz
                                <a style="font-weight:400;" href="https://kreosus.com/yilbasicekilisi">bu bağlantıyı </a>kullanabilirsiniz.
                            </p>
                        </div>
                    </td>
                </tr>
            </table>
        """

        msg.html = msg.body
        mail.send(msg)


@app.route("/", methods=["POST"])
def hello_world():
    email_list = []
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
    # elif request.args:
    #     r = request.args.to_dict()
    #     print(r)
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
