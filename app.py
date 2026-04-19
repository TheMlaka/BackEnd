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
databaza = {
    "students": [
        {"id": 1, "name": "Rastislav", "surname": "Paták", "nickname": "Kašlík", "personality": "very shy", "image": "https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg"},
        {"id": 2, "name": "Daniel", "surname": "Barta", "nickname": "Bart", "personality": "acts very smart and mature", "image": "https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg"}
    ]
}


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
