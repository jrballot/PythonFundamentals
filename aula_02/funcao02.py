#!/usr/bin/env python3

def get_input_as_int(mensagem, error):
	user_input = input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(error)

def tratamento_de_tentativas(numero_tentativas, mensagem, erro):
	for tentativa in range(numero_tentativas):
		try:
			return get_input_as_int(mensagem, erro)
		except ValueError as error:
			restante = numero_tentativas - (tentativa + 1)
			print('Um erro aconteceu.Voce tem {} tentativas restantes'.format(\
					restante))
			print(error)
	print('Voce errou o input {} vezes.'.format(numero_tentativas))
	print('Vou encerrar o programa')

#value_returned = get_input_as_int(
#	'Caso de teste: ',
#	'Deve ser um numero !!!'
#	)

valor_retorno = tratamento_de_tentativas(
		10,
		'Caso de teste: ',
		'Deve ser um numero'
	)


print(valor_retorno)
