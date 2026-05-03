import os
import psycopg2

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))


def create_table():
    conn = get_db()
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

    print("✅ TABLE READY")


def seed_data():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students;")
    count = cur.fetchone()[0]

    if count == 0:
        cur.execute("""
        INSERT INTO students (name, surname, nickname, personality, image)
        VALUES
        ('Rastislav','Paták','Kašlík','you are very shy','https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg'),
        ('Daniel','Barta','Bart','you love pcs and drones','https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg'),
        ('Samuel','Martiš','Žukva','you love cats and music','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bG2cU0TXNW')
        ;
        """)
        conn.commit()
        print("🔥 DATA SEEDED")

    cur.close()
    conn.close()
