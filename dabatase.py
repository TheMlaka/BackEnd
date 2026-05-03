import psycopg2

def main():
    conn = psycopg2.connect(
        database="mariadb_yri6",
        user="mariadb_yri6_user",
        password="SEM_DAJ_NOVÉ_HESLO",
        host="dpg-d7ng3t6gvqtc73ar4g00-a.frankfurt-postgres.render.com",
        port=5432
    )

    cur = conn.cursor()

    # 🧱 CREATE TABLE
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

    print("✅ TABLE CREATED!")

    cur.close()
    conn.close()


# 👉 TOTO JE DÔLEŽITÉ
if __name__ == "__main__":
    main()
