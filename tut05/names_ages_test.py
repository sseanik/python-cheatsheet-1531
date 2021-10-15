import pytest
import requests

URL = "http://127.0.0.1:5000"

@pytest.fixture()
def setup():
    requests.delete(f"{URL}/clearpeople")

@pytest.fixture
def add_sean():
    response = requests.post(f"{URL}/addperson", json={
        "name": "Sean",
        "dob": "01-01-2000"
    })
    assert response.status_code == 200
    assert response.json() == {}

def test_add_person(setup, add_sean):
    response = requests.post(f"{URL}/addperson", json={
        "name": "Sean",
        "dob": "01-01-2000"
    })
    assert response.status_code == 200
    assert response.json() == {}

def test_get_people(setup, add_sean):
    response_get = requests.get(f"{URL}/getpeople")
    response_get.status_code == 200
    response_get.json() == [{
        "name": "Sean",
        "age": 21
    }]
    

def test_clear_people(add_sean):
    response = requests.delete(f"{URL}/clearpeople")
    assert response.status_code == 200
    assert response.json() == {}

    response_get = requests.get(f"{URL}/getpeople")
    assert response_get.status_code == 200
    assert response_get.json() == []