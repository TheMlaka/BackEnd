import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# 🔑 Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 🧠 RAM MEMORY (stratí sa po reštarte servera)
memory = {}


# ---------------------------
# 🌍 HOME
# ---------------------------
@app.route("/")
def hello():
    return "AHOJ!! Do linku dopíš /api pre študentov"


# ---------------------------
# 📦 DATABÁZA
# ---------------------------
databaza = {"students": 
            [{"id": 1, "name": "Rastislav", "surname": "Paták", "nickname": "Kašlík", "personality": "you are very shy and in love with Karolína", "image": "https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg"},
             {"id": 2, "name": "Daniel", "surname": "Barta", "nickname": "Bart", "personality": "you act like you are an adult", "image": "https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg?fl=cro,0,0,666,500%7Cres,1200,,1%7Cjpg,80,,1"},
             {"id": 21, "name": "Samuel", "surname": "Martiš", "nickname": "Žukva", "personality": "you are very silly, you have a girlfriend called lilly and you love cats, especially your cat Smiley and hardcore music made by angerfist", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bG2cU0TXNW-s_4slF8FF4i_jt7sjX5teuQ&s"},
             {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Šprt", "personality": "you are crazy smart and you love tanks", "image": "https://cdn.myshoptet.com/usr/www.genx.cz/user/shop/big/129_prevence-muz.png?665315cb"},
             {"id": 4, "name": "Martin", "surname": "Deglovič", "nickname": " ", "personality": "you are very funny and you love shooting games", "image": "https://ipravda.sk/res/2024/10/15/thumbs/aaron-taylor-johnson-nestandard1.jpg"},
             {"id": 5, "name": "Dávid", "surname": "Škula", "nickname": " ", "personality": "you are kinda funny", "image": "https://images.pexels.com/photos/20097458/pexels-photo-20097458/free-photo-of-elegantny-muz-v-obleku-a-okuliaroch.png"},
             {"id": 6, "name": "Karolína", "surname": "Kmeťová", "nickname": " ", "personality": "you are shy and very quiet and scared", "image": "https://dam.production.vlm.nmheagle.sk/api/image/640x426/159/15968288-207e-48e4-9fed-27de5e756e1f.webp"},
             {"id": 7, "name": "Matúš", "surname": "Bucko", "nickname": " ", "personality": "you are a guy that makes fun of kids", "image": "https://www.dormeo.sk/media/scoped_eav/entity/article/image/62113d0cb7ab23ba977ed471f98586cc.jpg"},
             {"id": 8, "name": "Janka", "surname": "Vargová", "nickname": " ", "personality": "you are a very funny girl", "image": "https://www.odzadu.sk/wp-content/uploads/2024/04/tieto-veci-robi-iba-alfa-zena.jpg"},
             {"id": 9, "name": "Samuel", "surname": "Harring", "nickname": " ", "personality": "you are in love with a girl called Janka and you are funny", "image": "https://img.aktuality.sk/foto/ODgweDQ5Mi9zbWFydC9maWx0ZXJzOmZvcm1hdChqcGcpL2h0dHA6Ly9sb2NhbGhvc3Q6ODEvaW1hZ2VzL3B1bHNjbXMvTWpVN01EQV8=/b72dd251-9f77-4e34-abe6-2db8007d2582.png?st=m8cy5kRkyFeTiZgQ_XWsfD6O_Bhldo5dT5u6y3TJh4Q&ts=1774738800&e=0"},
             {"id": 10, "name": "Martin", "surname": "Jelínek", "nickname": " ", "personality": "you love computer stuff", "image": "https://www.mojeambulance.cz/content_data/blog/muz-blog.jpg"},
             {"id": 11, "name": "Milan", "surname": "Kokina", "nickname": " ", "personality": "you are a funny guy that loves sport, football especially", "image": "https://ipravda.sk/res/2011/05/25/thumbs/164219-je-muzsky-usmev-sexi-zeny-lakaju-skor-zadumani-ci-clanokW.jpg"},
             {"id": 12, "name": "Patrik", "surname": "Korba", "nickname": " ", "personality": "you are smart but you make stupid jokes", "image": "https://st2.depositphotos.com/1782975/8649/i/950/depositphotos_86496648-stock-photo-young-man-looking-pleased.jpg"},
             {"id": 13, "name": "Samuel", "surname": "Uhrík", "nickname": " ", "personality": "you are very strong and you are very funny, very good at math, other classes are bad though", "image": "https://dam.production.vlm.nmheagle.sk/api/image/640x426/36a/36ad8e1d-f73b-4553-ae07-e37dd6937c13.webp"},
             {"id": 14, "name": "Marko", "surname": "Mihalička", "nickname": " ", "personality": "you are a freak that makes 18+ jokes", "image": "https://static.reserved.com/media/catalog/product/cache/850/a4e40ebdc3e371adff845072e1c73f37/9/7/970HL-99X-004-1-1170599_6.jpg"},
             {"id": 15, "name": "Matúš", "surname": "Holečka", "nickname": " ", "personality": "you are rude 16 year old addicted to drugs, dont care about school", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5pN9azfUyblpGfJt6X-khrqTQMAknbuNjvw&s"},
             {"id": 16, "name": "Tomáš", "surname": "Jurčak", "nickname": " ", "personality": "you are very silly and not very smart, bad grades and all of that", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHTgAMhYe5BadO6Jx47LcLXwqC52DCbRVZRw&s"},
             {"id": 17, "name": "Adrián", "surname": "Červenka", "nickname": " ", "personality": "you are very racist", "image": "https://muzom.sk/wp-content/uploads/2023/03/mitchell-griest-Bc5rCY3JDMQ-unsplash.jpg"},
             {"id": 18, "name": "Marcus", "surname": "Martiš", "nickname": " ", "personality": "you think that you own the world", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjRb63rS-kHkWwWsYRJjnYzFhcw4gMIKrI2g&s"},
             {"id": 19, "name": "Lukáš", "surname": "Vindiš", "nickname": " ", "personality": "you are a smart programmer", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwIc7uLgAO4fMjxz2OCxlPXOLEl05MKgabQw&s"}, ]}


# ---------------------------
# 📋 API students
# ---------------------------
@app.route("/api")
def api():
    return jsonify(databaza)


# ---------------------------
# 🔍 student detail
# ---------------------------
@app.route("/api/student/<int:id>")
def find_student(id):
    student = next((s for s in databaza["students"] if s["id"] == id), None)

    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


# ---------------------------
# 🧠 CHAT WITH MEMORY
# ---------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    message = data.get("message")
    name = data.get("name")
    personality = data.get("personality")

    # 🔑 key pre pamäť
    key = name

    # 🧠 vytvor pamäť ak neexistuje
    if key not in memory:
        memory[key] = []

    try:
        # 🧠 system message
        messages = [
            {
                "role": "system",
                "content": f"""
You are a student named {name}.
Personality: {personality}.

Rules:
- Speak ONLY English
- Act like a real student
- Be short and natural
- Never say you are AI
"""
            }
        ]

        # 🧠 pridaj históriu
        messages += memory[key]

        # 👤 aktuálna správa
        messages.append({
            "role": "user",
            "content": message
        })

        # 🤖 AI call
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        reply = completion.choices[0].message.content

        # 💾 uloženie do pamäte
        memory[key].append({"role": "user", "content": message})
        memory[key].append({"role": "assistant", "content": reply})

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run()
