from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagens
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# Criar a 1ª página
@app.route("/")
def homepage():
    return render_template ("homepage.html")   

# roda o aplicativo
socketio.run(app, host="192.168.1.4")