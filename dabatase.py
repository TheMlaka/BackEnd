def create_table():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name TEXT,
        surname TEXT,
        nickname TEXT,
        personality TEXT,
        image TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("TABLE READY")
