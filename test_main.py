from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Try call /magic"}


def test_do_magic():
    response = client.get("/magic/Master")
    assert response.status_code == 200
    assert response.json() == {
        "result": "Hello Master!"
    }
