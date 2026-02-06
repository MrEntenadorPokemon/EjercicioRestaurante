from flask import Flask, render_template, json
import os

app = Flask(__name__)


@app.route('/')
def inicio():
    # Abrimos y leemos el archivo JSON
    ruta_json = os.path.join(app.root_path, 'platillos.json')
    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos_menu = json.load(f)

    # Pasamos los datos al HTML
    return render_template('index.html', menu=datos_menu)


if __name__ == '__main__':
    app.run(debug=True)