class Viagem:

	pk = 0
	nome = ""
	local = ""
	ida = ""
	volta = ""
	carro = ""
	onibus = ""
	aviao = ""

	def __init__(self,  
		model_pk	= "", 
		model_nome	= "", 
		model_local 	= "", 
		model_ida 		= "", 
		model_volta 	= "", 
		model_carro 	= "",
		model_onibus 	= "", 
		model_aviao 	= ""
		):

		self.pk = model_pk
		self.nome = model_nome
		self.local = model_local
		self.ida = model_ida
		self.volta = model_volta
		self.carro = model_carro
		self.onibus = model_onibus
		self.aviao = model_aviao

	def __str__(self):
		return f'#{self.pk} - {self.nome}'


class Evento:
	pk = 0
	nome_evento = ""
	data_inicio = ""
	data_final = ""
	categoria = ""
	endereco = ""
	noturno = ""
	diurno = ""
	integral = ""

	def __init__(self,
		model_pk 			="",
		model_nome_evento	="",
		model_data_inicio	="",
		model_data_final	="",
		model_categoria		="",
		model_endereco		="",
		model_noturno		="",
		model_diurno		="",
		model_integral		=""
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

	pk = 0
	nome_pessoa = ""
	idade = ""
	genero = ""
	cpf = ""

	def __init__(self,
		model_pk 			="",
		model_nome_pessoa	="",
		model_idade			="",
		model_genero		="",
		model_cpf			=""
		):

		self.pk = model_pk
		self.nome_pessoa = model_nome_pessoa
		self.idade = model_idade
		self.genero = model_genero
		self.cpf = model_cpf
