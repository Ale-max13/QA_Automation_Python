import os
import uuid
import requests
import pytest


BASE_URL = os.getenv(
    "YOUGILE_BASE_URL",
    "https://ru.yougile.com/api-v2",
).rstrip("/")
TOKEN = os.getenv("YOUGILE_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}

if not TOKEN:
    pytest.skip(
        "YOUGILE_TOKEN не задан (export/set перед запуском тестов).",
        allow_module_level=True,
    )


def test_get_project_get__200():
    r_create = requests.post(
        f"{BASE_URL}/projects",
        json={"title": f"autotest_{uuid.uuid4().hex[:8]}", "users": {}},
        headers=HEADERS,
    )
    assert r_create.status_code == 201, r_create.text
    project_id = r_create.json()["id"]

    r_get = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert r_get.status_code == 200, r_get.text
    assert r_get.json().get("id") == project_id


def test_get_project_get__404_unknown_id():
    bogus_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    r = requests.get(
        f"{BASE_URL}/projects/{bogus_id}",
        headers=HEADERS,
    )
    assert r.status_code == 404, r.text
