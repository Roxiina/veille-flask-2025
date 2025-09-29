from flask import Flask

# Création de l'application Flask
app = Flask(__name__)

# Route principale
@app.route('/')
def hello():
    # HTML direct
    return "Hello, Flask!"

# Route secondaire
@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour à tous !</h1><p>Voici une deuxième page servie directement par Flask.</p>"

# Route index
@app.route('/index')
def index():
    return render_template('index.html')

# Route name
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}"

# Route
@app.route('/perso/<name>')
def user(name):
    return render_template('index.html',username=name)
# Point d'entrée
if __name__ == "__main__":
    # Active le mode debug pour rechargement automatique
    app.run(debug=True)
