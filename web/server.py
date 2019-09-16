from flask import Flask, render_template, request, redirect
from model import Viagem


# http://bit.ly/2PfHiqX

app = Flask(__name__)

lista_viagens = []

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/listar_viagem")
def listar_viagem():
    
    nova_viagem = [
        Viagem("Leandro Klug", "São Paulo")
    ]    

    return render_template('listar_viagem.html', lista = lista_viagens)


@app.route("/form_inserir_viagem")
def form_inserir_viagem():
    return render_template("form_inserir_viagem.html")


@app.route("/incluir_viagem")
def incluir_viagem():
    
    #info básica
    form_nome = request.args.get("input_nome")
    form_local = request.args.get("input_local")
    form_ida = request.args.get("input_ida")
    form_volta = request.args.get("input_volta")

    # meios de transporte
    form_carro = request.args.get("input_carro")
    form_onibus = request.args.get("input_onibus")
    form_aviao = request.args.get("input_aviao")

    nova_viagem = Viagem(
        model_nome = form_nome, 
        model_local = form_local, 
        model_ida = form_ida, 
        model_volta = form_volta,
        model_carro = form_carro,
        model_onibus = form_onibus,
        model_aviao = form_aviao,
        )
    

    lista_viagens.append(nova_viagem)

    return render_template('success_msg.html', mensagem = f"Viagem {nova_viagem.nome} inserida!") 


@app.route("/form_alterar_viagem")
def form_alterar_viagem():

    nome = request.args.get("nome")

    for viagem in lista_viagens:

        if nome == viagem.nome:
            return render_template('form_alterar_viagem.html', viagem = viagem)

    return listar_viagem()        



@app.route("/alterar_viagem")
def alterar_viagem():

    nome = request.args.get("nome")
    local = request.args.get("local")
    ida = request.args.get("ida")
    volta = request.args.get("volta")

    indice = -1

    for i in range(len(lista_viagens)):
        if lista_viagens[i].nome == nome_original:
            indice = i
            break

    if indice >= 0:
        lista_viagens[indice] = Viagem(nome, local, ida, volta)        

    return listar_viagem()



@app.route("/excluir_viagem")
def excluir_viagem():

    excluir = None

    nome = request.args.get("nome")

    for viagem in lista_viagens:
        
        if nome == viagem.nome:
            excluir = viagem
            break

    if excluir != None:
        lista_viagens.remove(excluir)

    return listar_viagem()            


app.run(host="0.0.0.0", debug=True)
