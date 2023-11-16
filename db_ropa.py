import sqlite3
DATABASE_NAME = "ropa.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS ropa(
                ID INTEGER PRIMARY KEY,
                producto TEXT NOT NULL,
                precio INTEGER NOT NULL,
                stock INTEGER NOT NULL,
                material TEXT NOT NULL,
                color TEXT NOT NULL,
                tela TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
