import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from groq import Groq

from database import create_table, seed_data

app = Flask(__name__)
CORS(app)

# 🔑 GROQ
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 🧠 RAM memory
memory = {}

# 🔌 DB
def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))


# 🧱 INIT DB (pri štarte servera)
create_table()
seed_data()


# ---------------------------
# 🌍 HOME
# ---------------------------
@app.route("/")
def home():
    return "Backend running 🚀"


# ---------------------------
# 📋 GET ALL
# ---------------------------
@app.route("/api")
def get_students():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "nickname": row[3],
            "personality": row[4],
            "image": row[5]
        })

    cur.close()
    conn.close()

    return jsonify({"students": students})


# ---------------------------
# 🔍 GET BY ID
# ---------------------------
@app.route("/api/student/<int:id>")
def get_student(id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE id = %s", (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "nickname": row[3],
            "personality": row[4],
            "image": row[5]
        })

    return jsonify({"error": "Not found"}), 404


# ---------------------------
# ➕ ADD
# ---------------------------
@app.route("/api/student", methods=["POST"])
def add_student():
    data = request.json

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, surname, nickname, personality, image)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (
        data["name"],
        data["surname"],
        data.get("nickname"),
        data.get("personality"),
        data.get("image")
    ))

    new_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "added", "id": new_id})


# ---------------------------
# ❌ DELETE
# ---------------------------
@app.route("/api/student/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": "deleted"})


# ---------------------------
# 🧠 CHAT
# ---------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    message = data.get("message")
    name = data.get("name")
    personality = data.get("personality")

    key = name

    if key not in memory:
        memory[key] = []

    try:
        messages = [
            {
                "role": "system",
                "content": f"""
You are {name}.
Personality: {personality}.
Speak only English.
Be short and natural.
"""
            }
        ]

        messages += memory[key]

        messages.append({
            "role": "user",
            "content": message
        })

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        reply = completion.choices[0].message.content

        memory[key].append({"role": "user", "content": message})
        memory[key].append({"role": "assistant", "content": reply})

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------------------
# ▶️ RUN
# ---------------------------
if __name__ == "__main__":
    app.run()
