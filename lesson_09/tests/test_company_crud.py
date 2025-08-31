from sqlalchemy import text
from lesson_09.db import engine
import uuid
import pytest

@pytest.fixture(scope="session")
def db_conn():
    with engine.begin() as conn:
        yield conn

def _make_name(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def test_create_company(db_conn):
    name = _make_name("autotest_create")

    new_id = db_conn.execute(
        text("INSERT INTO company (name) VALUES (:n) RETURNING id"),
        {"n": name}
    ).scalar_one()

    got = db_conn.execute(
        text("SELECT name FROM company WHERE id = :id"),
        {"id": new_id}
    ).scalar_one()

    assert got == name

    db_conn.execute(text("DELETE FROM company WHERE id = :id"), {"id": new_id})

def test_update_company(db_conn):
    name = _make_name("autotest_update")
    company_id = db_conn.execute(
        text("INSERT INTO company (name) VALUES (:n) RETURNING id"),
        {"n": name}
    ).scalar_one()

    new_name = name + "_upd"
    db_conn.execute(
        text("UPDATE company SET name = :n WHERE id = :id"),
        {"n": new_name, "id": company_id}
    )

    got = db_conn.execute(
        text("SELECT name FROM company WHERE id = :id"),
        {"id": company_id}
    ).scalar_one()
    assert got == new_name

    db_conn.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})

def test_delete_company(db_conn):
    name = _make_name("autotest_delete")
    company_id = db_conn.execute(
        text("INSERT INTO company (name) VALUES (:n) RETURNING id"),
        {"n": name}
    ).scalar_one()

    db_conn.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})

    cnt = db_conn.execute(
        text("SELECT COUNT(*) FROM company WHERE id = :id"),
        {"id": company_id}
    ).scalar_one()
    assert cnt == 0
