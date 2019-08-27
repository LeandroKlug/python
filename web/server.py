from flask import Flask, render_template
from classe import Pessoa

# http://bit.ly/2PfHiqX

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/price")
def price():
    return render_template('price.html') 

@app.route("/people")
def people():
	
	    # popular com dados ficticios e depois jogar para inicio do arquivo
    pessoas = [
        Pessoa("João", "Blumenau", "São Paulo", "6", "1", "Avião"),
        Pessoa("Bruno", "Blumenau", "Rio de Janeiro", "12", "1", "Avião"),
        Pessoa("Maria", "Blumenau", "Curitiba", "2", "2", "Carro"),
        Pessoa("Creuza", "Blumenau", "Florianópolis", "1", "4", "Ônibus"),
        Pessoa("Carlos", "Blumenau", "Porto Alegre", "2", "3", "Avião"),
        Pessoa("Sidnei", "Blumenau", "Brasília", "7", "3", "Avião")
    ]

    return render_template('people.html', people = pessoas)       

app.run(debug=True)
