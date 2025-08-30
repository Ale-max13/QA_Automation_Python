import os
import uuid
import requests
import pytest

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2").rstrip("/")
TOKEN = os.getenv("YOUGILE_TOKEN")

HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}

@pytest.mark.skipif(not TOKEN, reason="YOUGILE_TOKEN не задан (export/set перед запуском тестов).")
def test_create_project_post():
    payload = {"title": f"autotest_{uuid.uuid4().hex[:8]}", "users": {}}
    r = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str) and body["id"]

@pytest.mark.skipif(not TOKEN, reason="YOUGILE_TOKEN не задан (export/set перед запуском тестов).")
def test_create_project_post__400_without_title():
    payload = {"users": {}}
    r = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    assert r.status_code == 400, r.text
