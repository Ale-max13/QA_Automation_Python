import os
import uuid
import requests
import pytest

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2").rstrip("/")
TOKEN = os.getenv("YOUGILE_TOKEN")

if not TOKEN:
    pytest.skip("YOUGILE_TOKEN не задан (export/set перед запуском тестов).", allow_module_level=True)

HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def test_update_project_put():
    create_payload = {"title": f"autotest_{uuid.uuid4().hex[:8]}", "users": {}}
    r_create = requests.post(f"{BASE_URL}/projects", json=create_payload, headers=HEADERS)
    assert r_create.status_code == 201, r_create.text
    project_id = r_create.json()["id"]

    new_title = create_payload["title"] + "_upd"
    r_put = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS,
    )
    assert r_put.status_code == 200, r_put.text
    assert r_put.json().get("id") == project_id


def test_update_project_put__404_unknown_id():
    bogus_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    r = requests.put(
        f"{BASE_URL}/projects/{bogus_id}",
        json={"title": "x"},
        headers=HEADERS,
    )
    assert r.status_code == 404, r.text


