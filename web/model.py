class Viagem:

	nome = ""
	local = ""
	ida = ""
	volta = ""
	carro = ""
	onibus = ""
	aviao = ""

	def __init__(self, 
		model_nome 		= "", 
		model_local 	= "", 
		model_ida 		= "", 
		model_volta 	= "", 
		model_carro 	= "",
		model_onibus 	= "", 
		model_aviao 	= ""
		):

		self.nome = model_nome
		self.local = model_local
		self.ida = model_ida
		self.volta = model_volta
		self.carro = model_carro
		self.onibus = model_onibus
		self.aviao = model_aviao


