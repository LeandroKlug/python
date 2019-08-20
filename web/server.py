from flask import Flask, render_template

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
    return render_template('people.html')       
	
	# popular com dados ficticios e depois jogar para inicio do arquivo
	pessoas=[
		Pessoa = ("001", "Blumenau", "São Paulo", "6", "1", "Avião")
	]

app.run(debug=True)
