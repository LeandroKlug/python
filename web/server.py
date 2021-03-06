from flask import Flask, render_template, request, redirect
from model import Viagem, Pessoa, Evento

app = Flask(__name__)

lista_viagens = []
lista_pessoas = []
lista_eventos = []

@app.route("/")
def index():
    return render_template('index.html')


 ########  ########  ######   ######   #######     ###    
 ##     ## ##       ##    ## ##    ## ##     ##   ## ##   
 ##     ## ##       ##       ##       ##     ##  ##   ##  
 ########  ######    ######   ######  ##     ## ##     ## 
 ##        ##             ##       ## ##     ## ######### 
 ##        ##       ##    ## ##    ## ##     ## ##     ## 
 ##        ########  ######   ######   #######  ##     ## 

@app.route("/listar_pessoa")
def listar_pessoa():
    return render_template('listar_pessoa.html', lista = lista_pessoas)


@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
    return render_template("form_inserir_pessoa.html")


@app.route("/incluir_pessoa")
def incluir_pessoa():
    
    #info básica
    form_nome_pessoa = request.args.get("input_nome_pessoa")
    form_idade = request.args.get("input_idade")
    form_genero = request.args.get("input_genero")
    form_cpf = request.args.get("input_cpf")

    nova_pessoa = Pessoa(
        model_pk = lista_pessoas[-1].pk + 1 if lista_pessoas else 1,
        model_nome_pessoa = form_nome_pessoa,
        model_idade = form_idade, 
        model_genero = form_genero, 
        model_cpf = form_cpf 
        )
    

    lista_pessoas.append(nova_pessoa)

    return render_template('success_pessoa.html', 
        mensagem = f"Pessoa {nova_pessoa.nome_pessoa} foi inserida com sucesso!") 


@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():

    nome_pessoa = request.args.get("nome_pessoa")

    for pessoa in lista_pessoas:

        if nome_pessoa == pessoa.nome_pessoa:
            return render_template('form_alterar_pessoa.html', 
                pessoa = pessoa)

    return listar_pessoa        



@app.route("/alterar_pessoa")
def alterar_pessoa():

    nome_pessoa = request.args.get("nome_pessoa")
    idade = request.args.get("idade")
    genero = request.args.get("genero")
    cpf = request.args.get("cpf")

    for i in range(len(lista_pessoas)):
        if lista_pessoas[i].nome_pessoa == nome_original:
            indice = i
            break

    if indice >= 0:
        lista_pessoas[indice] = Pessoa(nome_pessoa,
                                    idade,
                                    ida,
                                    volta)        

    return listar_pessoa()



@app.route("/excluir_pessoa")
def excluir_pessoa():

    excluir = None

    nome_pessoa = request.args.get("nome_pessoa")

    for pessoa in lista_pessoas:
        
        if nome_pessoa == pessoa.nome_pessoa:
            excluir = pessoa
            break

    if excluir != None:
        lista_pessoas.remove(excluir)

    return listar_pessoa()



 ##     ## ####    ###     ######   ######## ##     ## 
 ##     ##  ##    ## ##   ##    ##  ##       ###   ### 
 ##     ##  ##   ##   ##  ##        ##       #### #### 
 ##     ##  ##  ##     ## ##   #### ######   ## ### ## 
  ##   ##   ##  ######### ##    ##  ##       ##     ## 
   ## ##    ##  ##     ## ##    ##  ##       ##     ## 
    ###    #### ##     ##  ######   ######## ##     ## 


@app.route("/listar_viagem")
def listar_viagem():
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
        model_pk = lista_viagens[-1].pk + 1 if lista_viagens else 1,
        model_nome = form_nome, 
        model_local = form_local, 
        model_ida = form_ida, 
        model_volta = form_volta,
        model_carro = form_carro,
        model_onibus = form_onibus,
        model_aviao = form_aviao,
        )
    

    lista_viagens.append(nova_viagem)

    return render_template('success_viagem.html', 
        mensagem = f"Viagem {nova_viagem.nome} inserida!") 


@app.route("/form_alterar_viagem")
def form_alterar_viagem():

    pos = request.args.get("pos")

    for viagem in lista_viagens:

        if int(pos) == viagem.pk:
            return render_template('form_alterar_viagem.html', 
                viagem = viagem)

    return listar_viagem()        



@app.route("/alterar_viagem")
def alterar_viagem():

    nome = request.args.get("nome")
    local = request.args.get("local")
    ida = request.args.get("ida")
    volta = request.args.get("volta")

    pk = int(request.args.get("pk"))

    for viagem in lista_viagens:
        if viagem.pk == pk:
            lista_viagens[viagem.pk - 1] = Viagem(pk, nome, local, ida, volta)
            break
                

    return listar_viagem()



@app.route("/excluir_viagem")
def excluir_viagem():

    excluir = None

    pos = request.args.get("pos")

    for viagem in lista_viagens:
        if viagem.pk == int(pos):
            excluir = viagem
            break

    if excluir != None:
        lista_viagens.remove(excluir)

    return listar_viagem()


 ######## ##     ## ######## ##    ## ########  #######  
 ##       ##     ## ##       ###   ##    ##    ##     ## 
 ##       ##     ## ##       ####  ##    ##    ##     ## 
 ######   ##     ## ######   ## ## ##    ##    ##     ## 
 ##        ##   ##  ##       ##  ####    ##    ##     ## 
 ##         ## ##   ##       ##   ###    ##    ##     ## 
 ########    ###    ######## ##    ##    ##     #######  


@app.route("/listar_evento")
def listar_evento():
    
    novo_evento = []    

    return render_template('listar_eventos.html', lista = lista_eventos)


@app.route("/form_inserir_evento")
def form_inserir_evento():
    return render_template("form_inserir_evento.html")


@app.route("/incluir_evento")
def incluir_evento():
    
    # info básica 
    form_pk = request.args.get("input_pk")
    form_nome_evento = request.args.get("input_nome_evento")
    form_data_inicio = request.args.get("input_data_inicio")
    form_data_final = request.args.get("input_data_final")
    form_categoria = request.args.get("input_categoria")
    form_endereco = request.args.get("input_endereco")

    # horário do evento
    form_noturno = request.args.get("input_noturno")
    form_diurno = request.args.get("input_diurno")
    form_integral = request.args.get("input_integral")

    novo_evento = Evento(
        model_pk = form_pk,
        model_nome_evento = form_nome_evento, 
        model_data_inicio = form_data_inicio, 
        model_data_final = form_data_final, 
        model_categoria = form_categoria,
        model_endereco = form_endereco,
        model_noturno = form_noturno,
        model_diurno = form_diurno,
        model_integral = form_integral
        )
    

    lista_eventos.append(novo_evento)

    return render_template('success_evento.html', 
        mensagem = f"Evento {novo_evento.nome_evento} inserida!") 


@app.route("/form_alterar_evento")
def form_alterar_evento():

    nome_evento = request.args.get("nome_evento")

    for evento in lista_eventos:

        if nome_evento == evento.nome_evento:
            return render_template('form_alterar_viagem.html', 
                evento = evento)

    return listar_evento()        



@app.route("/alterar_evento")
def alterar_evento():

    nome_evento = request.args.get("nome_evento")
    data_inicio = request.args.get("data_inicio")
    data_final = request.args.get("data_final")
    categoria = request.args.get("categoria")
    endereco = request.args.get("endereco")
    noturno = request.args.get("noturno")
    diurno = request.args.get("diurno")
    integral = request.args.get("integral")

    indice = -1

    for i in range(len(lista_eventos)):
        if lista_eventos[i].nome_original == nome_original:
            indice = i
            break

    if indice >= 0:
        lista_eventos[indice] = Evento(nome_evento, data_inicio, data_final,
                                        categoria, endereco, noturno, diurno, integral)        

    return listar_evento()



@app.route("/excluir_evento")
def excluir_evento():

    excluir = None

    nome_evento = request.args.get("nome_evento")

    for evento in lista_eventos:
        
        if nome_evento == evento.nome_evento:
            excluir = evento
            break

    if excluir != None:
        lista_eventos.remove(excluir)

    return listar_evento()


app.run(host="0.0.0.0", debug=True)
