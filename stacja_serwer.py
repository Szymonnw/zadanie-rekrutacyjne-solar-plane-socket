from flask import Flask, request, render_template
import os
from flask_socketio import SocketIO

if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

UPLOAD_FOLDER = 'static/uploads'

ostatnia_wiadomosc = "oczekiwanie na wiadomosc"
ostatnie_zdj = None


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html', msg = ostatnia_wiadomosc, img = ostatnie_zdj)

@app.route('/upload', methods=['POST'])
def upload():
    global ostatnia_wiadomosc, ostatnie_zdj
    wiadomosc = request.form.get('tekst')
    plik = request.files.get('zdjecie')

    if plik and wiadomosc:
        ostatnia_wiadomosc = wiadomosc
        ostatnie_zdj = plik.filename
        sciezka = os.path.join(UPLOAD_FOLDER, plik.filename)
        plik.save(sciezka)
        socketio.emit('nowe_dane',
            {'wiadomosc': wiadomosc,
             'zdjecie_url': plik.filename})
        
        return "Stacja : odebrano zdjecie i komunikat!", 200
        
    return "brakuje zdjecia lub komunikatu", 400



if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)

    