#!/usr/bin/env python3


lista_de_gatos = [
        {
            'nome': 'Acer',
            'peso': 5000,
            'idade': 6,
            'apelido': 'sedoso'
        },
        {
            'nome':'fernando',
            'peso': 3000,
            'idade': 2,
            'apelido': 'brilhoso'
        }
    ]


def get_input_as_int(mensagem):
	user_input = input(mensagem)
	
	for token in user_input:
		print("Candidator atual: {}".format(token))
		if token not in '1234567890':
			return -1

	#if user_input.isdigit():
	#	return int(user_input)
	return int(user_input)

novo_gato = {
		'nome': input('Nome do gato: '),
		'peso': get_input_as_int('Digite o peso: '),
		'idade': get_input_as_int('Digite a idade: '),
		'apelido': input('Apelido do gato: ')
	}
lista_de_gatos.append(novo_gato)

for gato in lista_de_gatos:
	if gato['peso'] > 4000:
		print('Gato com mais de 4000g encontrado')
		print('{} pesa {} e possui o apelido de {}'.format(gato['nome'], \
														gato['peso'], \
														gato['apelido']))        

print(novo_gato)
