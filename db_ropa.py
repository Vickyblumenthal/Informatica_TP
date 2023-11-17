import sqlite3
DATABASE_NAME = "ropa.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS productos(
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

    # Verifica la existencia de la tabla
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='productos';")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Si la tabla no existe, intenta crearla
        cursor.execute(tables[0])

    db.commit()
    db.close()
