import uuid
import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "rBFeKGxHCPCEln5iMe-HypPZYHDJkjdLSj4YqxvlhKIA+r2XzYmQHiaA+WsRUwki"

def test_create_project_post():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": f"autotest_{uuid.uuid4().hex[:8]}",
        "users": {}
    }
    r = requests.post(url, json=payload, headers={"Authorization": f"Bearer {TOKEN}"})
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str) and body["id"], "В ответе нет id созданного проекта"
