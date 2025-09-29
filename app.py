from flask import Flask

app = Flask(__name__)

@app.route('/bonjour')
def bonjour():
    return "<h2>Bonjour à tous !</h2>"

@app.route('/')
def hello():
    # Retour direct d'un code HTML
    return "<h1>Hello, Flask!</h1><p>Bienvenue sur votre première page HTML servie directement !</p>"