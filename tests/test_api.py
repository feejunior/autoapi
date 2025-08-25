import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    """Teste básico de GET"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    body = response.json()
    assert "userId" in body
    assert body["id"] == 1


def test_create_post():
    """Teste básico de POST"""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "foo"
    assert body["body"] == "bar"
