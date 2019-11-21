from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/CEL_0071.jpg/1024px-CEL_0071.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Fuente_de_los_peces_%28Almer%C3%ADa%29.jpg/1024px-Fuente_de_los_peces_%28Almer%C3%ADa%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Fuente_de_los_delfines_01.jpg/1024px-Fuente_de_los_delfines_01.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Fuente_del_remador_02.jpg/1024px-Fuente_del_remador_02.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/La_Isleta_del_Moro.jpg/1024px-La_Isleta_del_Moro.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Los_volcanes_de_Los_Frailes.jpg/1024px-Los_volcanes_de_Los_Frailes.jpg"
]

texts = [
    "bla bla bla",
    "ble ble ble",
    "bli bli bli",
    "blo blo blo",
    "blu blu blu"
]

@app.route('/')
def index():
    url = random.choice(images)
    text = random.choice(texts)
    return render_template('index.html', url=url, text=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")