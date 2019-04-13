#!/usr/bin/env python3

lista_de_gatos = []

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


novo_gato = {
		'nome': input('Nome do gato: '),
		'peso': tratamento_de_tentativas(
				5,
				'Digite o peso: ',
				'O peso deve ser maior que 0.'),
		'idade': tratamento_de_tentativas(
				5,
				'Digite a idade: ',
				'A idade deve ser maior que 0.'),
		'apelido': input('Apelido do gato: ')
	}

lista_de_gatos.append(novo_gato)

for gato in lista_de_gatos:
	if gato['peso'] > 4000:
		print('Gato com mais de 4000g encontrado')
		print('{} pesa {} e possui o apelido de {}'.format(gato['nome'], \
														gato['peso'], \
														gato['apelido']))        

