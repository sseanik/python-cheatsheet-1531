import pytest
import requests

def test_comment():
    response = requests.post("http://127.0.0.1:5000/postcomment", json={
        "name": "Sean"
    })
    assert response.json() == {"name": "Sean"}
    assert response.status_code == 200
    # 200 == SUCCESS


    response_2 = requests.post("http://127.0.0.1:5000/postcomment", json={
        "dob": "Goose"
    })
    assert response_2.status_code == 500
