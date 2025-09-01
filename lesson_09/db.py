from sqlalchemy import create_engine, text

DB_URL = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
engine = create_engine(DB_URL)


def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        print("DB connection OK:", result)


if __name__ == "__main__":
    test_connection()
