from flask import Flask, render_template, request
from model import Viagem

# http://bit.ly/2PfHiqX

app = Flask(__name__)

viagens = []

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/listar_viagem")
def listar_viagem():
    
    viagem = [
        Viagem("Leandro Klug", "São Paulo")
    ]    

    return render_template('listar_viagem.html', lista = viagens)


@app.route("/form_inserir_viagem")
def form_inserir_viagem():
    return render_template("form_inserir_viagem.html")


@app.route("/incluir_viagem")
def incluir_viagem():
    
    nome = request.args.get("nome")
    local = request.args.get("local")
    inicio = request.args.get("inicio")
    volta = request.args.get("volta")

    new = Viagem(nome, local, inicio, volta)
    viagens.append(new)

    return render_template('success_msg.html', mensagem = "Viagem inserida!") 


@app.route("/form_alterar_viagem")
def form_alterar_viagem():

    nome = request.args.get("nome")

    for viagem in viagens:

        if nome == viagem.nome:
            return render_template('form_alterar_viagem', pessoa = viagem)

    return listar_viagem()        



@app.route("/alterar_viagem")
def alterar_viagem():

    nome = request.args.get("nome")
    local = request.args.get("local")
    ida = request.args.get("ida")
    volta = request.args.get("volta")

    indice = -1

    for i in range(len(viagem)):
        if viagem[i].nome == nome_original:
            indice = i
            break

    if indice >= 0:
        viagem[indice] = Viagem(nome, local, inicio, volta)        

    return redirect(listar_viagem)



@app.route("/excluir_viagem")
def excluir_viagem():

    excluir = None

    nome = request.args.get("nome")

    for viagem in viagens:
        
        if nome == viagem.nome:
            excluir = viagem
            break

    if excluir != None:
        viagens.remove(excluir)

    return listar_viagem()            


app.run(host="0.0.0.0", debug=True)
