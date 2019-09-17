class Viagem:

	local = ""
	ida = ""
	volta = ""
	carro = ""
	onibus = ""
	aviao = ""

	def __init__(self,  
		model_local 	= "", 
		model_ida 		= "", 
		model_volta 	= "", 
		model_carro 	= "",
		model_onibus 	= "", 
		model_aviao 	= ""
		):

		self.local = model_local
		self.ida = model_ida
		self.volta = model_volta
		self.carro = model_carro
		self.onibus = model_onibus
		self.aviao = model_aviao


class Evento:

	nome_evento = ""
	data_inicio = ""
	data_final = ""
	categoria = ""
	endereco = ""

	def __init__(self,
		model_nome_evento,
		model_data_inicio,
		model_data_final,
		model_categoria,
		model_endereco,
		model_noturno,
		model_diurno,
		model_integral
		):

		self.nome_evento = model_nome_evento
		self.data_inicio = model_data_inicio
		self.data_final = model_data_final
		self.categoria = model_categoria
		self.endereco = model_endereco
		self.noturno = model_noturno
		self.diurno = model_diurno
		self.integral = model_integral


class Pessoa:

	nome_pessoa = ""
	idade = ""
	genero = ""
	cpf = ""

	def __init__(self,
		model_nome_pessoa,
		model_idade,
		model_genero,
		model_cpf
		):

		self.nome_pessoa = model_nome_pessoa
		self.idade = model_idade
		self.genero = model_genero
		self.cpf = model_cpf
