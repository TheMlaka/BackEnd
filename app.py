from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 🔑 TU DAJ SVOJ API KEY
client = OpenAI(api_key="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")


@app.route('/')
def hello():
    return 'AHOJ!! Do linku dopíš /api pre zobrazenie študentov'


# 📦 DATABÁZA
databaza = {
    "students": [
        {"id": 1, "name": "Rastislav", "surname": "Paták", "nickname": "Kašlík", "personality": "si veľmi hanblivý", "image": "https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg"},
        {"id": 2, "name": "Daniel", "surname": "Barta", "nickname": "Bart", "personality": "správaš sa ako dospelý a robíš sa moc múdry", "image": "https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg"},
        {"id": 21, "name": "Samuel", "surname": "Martiš", "nickname": "Žukva", "personality": "si veľmi vtipný a robíš hlúpe vtipy", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bG2cU0TXNW-s_4slF8FF4i_jt7sjX5teuQ&s"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Šprt", "personality": "si prehnane múdry", "image": "https://cdn.myshoptet.com/usr/www.genx.cz/user/shop/big/129_prevence-muz.png"}
    ]
}


# 📋 ZOZNAM
@app.route("/api")
def api():
    return jsonify(databaza)


# 🔍 DETAIL ŠTUDENTA (opravené)
@app.route('/api/student/<int:id>')
def find_student(id):
    student = next((s for s in databaza["students"] if s["id"] == id), None)

    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404


# 🤖 AI CHAT
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    message = data.get("message")
    name = data.get("name")
    personality = data.get("personality")

    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Si študent menom {name}.
Tvoja osobnosť: {personality}.

Odpovedaj ako reálny študent.
Nepíš že si AI.
Buď prirodzený, krátky a autentický.
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


if __name__ == "__main__":
    app.run(debug=True)
