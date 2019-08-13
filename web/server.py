from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return '<a href="proxima">Clicar aqui</a>'

@app.route("/proxima")
def proxima():
    return '<a href="/">Clique de volta</a>'

app.run(debug=True)
