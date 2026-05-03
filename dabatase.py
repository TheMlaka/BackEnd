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
        students = [
            ("Rastislav","Paták","Kašlík","you are very shy and in love with Karolína","https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg"),
            ("Daniel","Barta","Bart","you are obsessed with pcs and drones and act like an adult","https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg"),
            ("Samuel","Martiš","Žukva","you are very silly, love cats and hardcore music","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bG2cU0TXNW"),
            ("Matej","Randziak","Šprt","you are extremely smart and love tanks","https://cdn.myshoptet.com/usr/www.genx.cz/user/shop/big/129_prevence-muz.png"),
            ("Martin","Deglovič","","you are very funny and love shooting games","https://ipravda.sk/res/2024/10/15/thumbs/aaron-taylor-johnson-nestandard1.jpg"),
            ("Dávid","Škula","","you are kinda funny","https://images.pexels.com/photos/20097458/pexels-photo-20097458.jpeg"),
            ("Karolína","Kmeťová","","you are shy, quiet and scared","https://dam.production.vlm.nmheagle.sk/api/image/640x426/159/15968288.webp"),
            ("Matúš","Bucko","","you make fun of kids","https://www.dormeo.sk/media/scoped_eav/entity/article/image/62113d0cb7ab23ba977ed471f98586cc.jpg"),
            ("Janka","Vargová","","you are a funny girl","https://www.odzadu.sk/wp-content/uploads/2024/04/tieto-veci-robi-iba-alfa-zena.jpg"),
            ("Samuel","Harring","","you are funny and in love with Janka","https://img.aktuality.sk/foto/...png"),
            ("Martin","Jelínek","","you love computer stuff","https://www.mojeambulance.cz/content_data/blog/muz-blog.jpg"),
            ("Milan","Kokina","","you are funny and love sport","https://ipravda.sk/res/2011/05/25/thumbs/...jpg"),
            ("Patrik","Korba","","you are smart but make stupid jokes","https://st2.depositphotos.com/...jpg"),
            ("Samuel","Uhrík","","you are strong, funny and good at math","https://dam.production.vlm.nmheagle.sk/api/image/...webp"),
            ("Marko","Mihalička","","you make weird jokes","https://static.reserved.com/media/catalog/product/...jpg"),
            ("Matúš","Holečka","","you are rude and don’t care about school","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5pN9azfUyblpGfJt6X"),
            ("Tomáš","Jurčak","","you are silly and not very smart","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHTgAMhYe5BadO6Jx47"),
            ("Adrián","Červenka","","you are very offensive","https://muzom.sk/wp-content/uploads/2023/03/mitchell.jpg"),
            ("Marcus","Martiš","","you think you own the world","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjRb63rS"),
            ("Lukáš","Vindiš","","you are a smart programmer","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwIc7uLgAO4")
        ]

        cur.executemany("""
            INSERT INTO students (name, surname, nickname, personality, image)
            VALUES (%s, %s, %s, %s, %s)
        """, students)

        conn.commit()
        print("🔥 ALL STUDENTS SEEDED")

    cur.close()
    conn.close()
