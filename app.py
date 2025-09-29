from flask import Flask, render_template

app = Flask(__name__)

# Route principale -> Hello HTML
@app.route('/')
def hello():
    return render_template('hello.html')

# Route secondaire -> Bonjour
@app.route('/bonjour')
def bonjour():
    return render_template('bonjour.html')

# Route index -> Menu général
@app.route('/index')
def index():
    return render_template('index.html', username=None)

# Route simple avec nom
@app.route('/user/<name>')
def user(name):
    return f"<h2>Hello, {name}!</h2><p><a href='/index'>Retour à l'index</a></p>"

# Route avec nom via template
@app.route('/perso/<name>')
def perso(name):
    return render_template('index.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)
