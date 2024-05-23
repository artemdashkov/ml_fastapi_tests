from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """
    Checking text on the main page
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}, "text is not 'Hello World'"


def test_predict_positive():
    """
    Positive test
    """
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE', "Text is not 'NEGATIVE' or 'NEUTRAL'"


def test_predict_negative():
    """
    Negative test
    """
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE', "Text is not 'POSITIVE' or 'NEUTRAL'"
