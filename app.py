import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


@app.route("/")
def hello():
    return "AHOJ!! Do linku dopíš /api pre zobrazenie študentov"


databaza = {
    "students": [
        {"id": 1, "name": "Rastislav", "surname": "Paták", "nickname": "Kašlík", "personality": "si veľmi hanblivý", "image": "..."}
    ]
}


@app.route("/api")
def api():
    return jsonify(databaza)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    message = data.get("message")
    name = data.get("name")
    personality = data.get("personality")

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Si študent menom {name}.
Tvoja osobnosť: {personality}.

Odpovedaj ako reálny študent.
Nepíš že si AI.
Buď krátky a prirodzený.
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = completion.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/student/<int:id>")
def find_student(id):
    student = next((s for s in databaza["students"] if s["id"] == id), None)

    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run()
