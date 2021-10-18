import pytest
import requests

URL = "http://127.0.0.1:5000"


@pytest.fixture()
def setup():
    requests.delete(f"{URL}/clearPeople")


@pytest.fixture()
def add_single_user(setup):
    response = requests.post(
        f"{URL}/addPerson", json={"name": "Sean", "dob": "01-01-2000"}
    )
    return response


@pytest.fixture()
def add_multiple_users(add_single_user):
    response_1 = requests.post(
        f"{URL}/addPerson", json={"name": "Hayden", "dob": "01-01-2005"}
    )
    response_2 = requests.post(
        f"{URL}/addPerson", json={"name": "Miguel", "dob": "01-01-2015"}
    )
    return [add_single_user, response_1, response_2]


def test_add_person(add_single_user):
    assert add_single_user.status_code == 200
    assert add_single_user.json() == {}


def test_add_people(add_multiple_users):
    for response in add_multiple_users:
        assert response.status_code == 200
        assert response.json() == {}


def test_get_singular_person(add_single_user):
    response = requests.get(f"{URL}/getPeople")
    response.status_code == 200
    response.json() == [{"name": "Sean", "age": 21}]


def test_get_multiple_people(add_multiple_users):
    response = requests.get(f"{URL}/getPeople")
    response.status_code == 200
    response.json() == [
        {"name": "Sean", "dob": "01-01-2000"},
        {"name": "Hayden", "dob": "01-01-2000"},
    ]


def test_clear_people(add_multiple_users):
    response = requests.delete(f"{URL}/clearPeople")
    assert response.status_code == 200
    assert response.json() == {}


def test_edit_user(add_single_user):
    response = requests.put(
        f"{URL}/editPerson", json={"name": "Hayden", "dob": "05-05-2010"}
    )
    response.status_code == 200
    response.json() == [{"name": "Hayden", "age": 11}]


def test_get_people_minimum_age_params(add_multiple_users):
    response = requests.get(f"{URL}/getPeople", params={"min_age": 10})
    response.status_code == 200
    response.json() == [
        {"name": "Sean", "dob": "01-01-2000"},
        {"name": "Hayden", "dob": "01-01-2005"},
    ]


def test_get_people_minimum_age_query_string(add_multiple_users):
    response = requests.get(f"{URL}/getPeople?min_age=10")
    response.status_code == 200
    response.json() == [
        {"name": "Sean", "dob": "01-01-2000"},
        {"name": "Hayden", "dob": "01-01-2005"},
    ]
