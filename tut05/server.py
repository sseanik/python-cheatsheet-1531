from typing import Protocol
from flask import Flask, request
from json import dumps


# Testing pytest
import requests

APP = Flask(__name__)

@APP.route('/auth/login/v2', methods=["POST"])
def get_comments():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    token, auth_user_id = auth_login(email, password)

    return dumps({"token": token, "auth_user_id": auth_user_id})


if __name__ == "__main__":
    APP.run(debug=True)