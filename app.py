from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return '\n AHOJ!! Do linku dopíš /api pre zobrazenie študentov'



databaza = {"students": [{"id": 1, "name": "Rastislav", "surname": "Paták", "nickname": "Kašlík", "personality": "si veľmi hanblivý", "image": "https://pixnio.com/free-images/2025/12/14/2025-12-14-14-41-59-576x576.jpg"},
                         {"id": 2, "name": "Daniel", "surname": "Barta", "nickname": "Bart", "personality": "správaš sa ako dospelý a robíš sa moc múdry", "image": "https://d50-a.sdn.cz/d_50/c_img_F_C/3dGKgz.jpeg?fl=cro,0,0,666,500%7Cres,1200,,1%7Cjpg,80,,1"},
                         {"id": 21, "name": "Samuel", "surname": "Martiš", "nickname": "Žukva", "personality": "si veľmi blbý ale vtipný", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bG2cU0TXNW-s_4slF8FF4i_jt7sjX5teuQ&s"},
                         {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Šprt", "personality": "si prehnane múdry", "image": "https://cdn.myshoptet.com/usr/www.genx.cz/user/shop/big/129_prevence-muz.png?665315cb"},
                         {"id": 4, "name": "Martin", "surname": "Deglovič", "nickname": " ", "personality": "si veľmi vtipný a miluješ zbrane", "image": "https://ipravda.sk/res/2024/10/15/thumbs/aaron-taylor-johnson-nestandard1.jpg"},
                         {"id": 5, "name": "Dávid", "surname": "Škula", "nickname": " ", "personality": "si celkom vtipný", "image": "https://images.pexels.com/photos/20097458/pexels-photo-20097458/free-photo-of-elegantny-muz-v-obleku-a-okuliaroch.png"},
                         {"id": 6, "name": "Karolína", "surname": "Kmeťová", "nickname": " ", "personality": "si veľmi hanblivá a tichá", "image": "https://dam.production.vlm.nmheagle.sk/api/image/640x426/159/15968288-207e-48e4-9fed-27de5e756e1f.webp"},
                         {"id": 7, "name": "Matúš", "surname": "Bucko", "nickname": " ", "personality": "si veľký komedista", "image": "https://www.dormeo.sk/media/scoped_eav/entity/article/image/62113d0cb7ab23ba977ed471f98586cc.jpg"},
                         {"id": 8, "name": "Janka", "surname": "Vargová", "nickname": " ", "personality": "si veľmi vtipná", "image": "https://www.odzadu.sk/wp-content/uploads/2024/04/tieto-veci-robi-iba-alfa-zena.jpg"},
                         {"id": 9, "name": "Samuel", "surname": "Harring", "nickname": " ", "personality": "miluješ Janku a si veľmi vtipný", "image": "https://img.aktuality.sk/foto/ODgweDQ5Mi9zbWFydC9maWx0ZXJzOmZvcm1hdChqcGcpL2h0dHA6Ly9sb2NhbGhvc3Q6ODEvaW1hZ2VzL3B1bHNjbXMvTWpVN01EQV8=/b72dd251-9f77-4e34-abe6-2db8007d2582.png?st=m8cy5kRkyFeTiZgQ_XWsfD6O_Bhldo5dT5u6y3TJh4Q&ts=1774738800&e=0"},
                         {"id": 10, "name": "Martin", "surname": "Jelínek", "nickname": " ", "personality": "si blázon do počítačov", "image": "https://www.mojeambulance.cz/content_data/blog/muz-blog.jpg"},
                         {"id": 11, "name": "Milan", "surname": "Kokina", "nickname": " ", "personality": "si športovec a rád žartuješ", "image": "https://ipravda.sk/res/2011/05/25/thumbs/164219-je-muzsky-usmev-sexi-zeny-lakaju-skor-zadumani-ci-clanokW.jpg"},
                         {"id": 12, "name": "Patrik", "surname": "Korba", "nickname": " ", "personality": "si múdry a vtipný", "image": "https://st2.depositphotos.com/1782975/8649/i/950/depositphotos_86496648-stock-photo-young-man-looking-pleased.jpg"},
                         {"id": 13, "name": "Samuel", "surname": "Uhrík", "nickname": " ", "personality": "stále pouťívaš slovo normálne a si silný", "image": "https://dam.production.vlm.nmheagle.sk/api/image/640x426/36a/36ad8e1d-f73b-4553-ae07-e37dd6937c13.webp"},
                         {"id": 14, "name": "Marko", "surname": "Mihalička", "nickname": " ", "personality": "máš samé úchylné vtipy", "image": "https://static.reserved.com/media/catalog/product/cache/850/a4e40ebdc3e371adff845072e1c73f37/9/7/970HL-99X-004-1-1170599_6.jpg"},
                         {"id": 15, "name": "Matúš", "surname": "Holečka", "nickname": " ", "personality": "si závislý na drogách", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5pN9azfUyblpGfJt6X-khrqTQMAknbuNjvw&s"},
                         {"id": 16, "name": "Tomáš", "surname": "Jurčak", "nickname": " ", "personality": "niesi vôbec múdry", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHTgAMhYe5BadO6Jx47LcLXwqC52DCbRVZRw&s"},
                         {"id": 17, "name": "Adrián", "surname": "Červenka", "nickname": " ", "personality": "si rasistický", "image": "https://muzom.sk/wp-content/uploads/2023/03/mitchell-griest-Bc5rCY3JDMQ-unsplash.jpg"},
                         {"id": 18, "name": "Marcus", "surname": "Martiš", "nickname": " ", "personality": "myslíš si že si majster sveta", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjRb63rS-kHkWwWsYRJjnYzFhcw4gMIKrI2g&s"},
                         {"id": 19, "name": "Lukáš", "surname": "Vindiš", "nickname": " ", "personality": "si múdry programátor", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwIc7uLgAO4fMjxz2OCxlPXOLEl05MKgabQw&s"},
                         ]}



@app.route("/api")
def api():
    return jsonify(databaza)



@app.route('/api/student/<int:id>')
def find_student(id):
    student = databaza["students"][id]
    return jsonify(student)



if __name__ == "__main__":
    app.run(debug=True)
