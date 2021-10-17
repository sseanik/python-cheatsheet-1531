from flask import Flask, request
from json import dumps
import names_ages

APP = Flask(__name__)


@APP.route("/addPerson", methods=["POST"])
def add_person():
    data = request.get_json()
    name, dob = data["name"], data["dob"]
    names_ages.add_name_age(name, dob)
    return {}


@APP.route("/getPeople", methods=["GET"])
def get_people():
    min_age = request.args.get('min_age')
    return dumps(names_ages.get_names_ages(min_age))


@APP.route("/clearPeople", methods=["DELETE"])
def clear_people():
    names_ages.clear_names_ages()
    return {}


@APP.route("/editPerson", methods=["PUT"])
def edit_person():
    data = request.get_json()
    name, dob = data["name"], data["dob"]
    names_ages.edit_name_age(name, dob)
    return {}


if __name__ == "__main__":
    APP.run(debug=True, port=5000)