from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
@app.route('/play')
def index():
    message = "Elige: Piedra, Papel o Tijera"
    return render_template('index.html', message=message)

@app.route('/play', methods=['POST'])
def play():
    opciones = ['Piedra', 'Papel', 'Tijera']
    usuario = request.form['choice']
    computadora = random.choice(opciones)
    resultado = ganador(usuario, computadora)

    return render_template('index.html', message=f'Elegiste: {usuario}, La Computadora eligió: {computadora}. {resultado}')
    

def ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "Piedra" and computadora == "Tijera") or (usuario == "Papel" and computadora == "Piedra") or (usuario == "Tijera" and computadora == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"

if __name__ == '__main__':
    app.run(debug=True)

