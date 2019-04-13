#!/usr/bin/env python3


import random
import string

def gerar_nome_aleatorio():
	return ''.join(
			random.choices(
					string.ascii_letters,
					k=random.randint(5,15)
				)
		)

	
def gerar_email_aleatorio():
	return ''.join(
			random.choices(
					string.ascii_letters,
					k=random.randint(5,15)
				)
		)


def gerar_idade_aleatorio():
	return random.randint(16,120)


def gerar_usuario_aleatorio():
	novo_usuario = {
			'nome': gerar_nome_aleatorio(), 				
			'email': gerar_email_aleatorio() + "@4linux.com.br", 				
			'idade': gerar_idade_aleatorio() 				
		}
	return novo_usuario


if __name__ == '__main__':
	usuario = gerar_usuario_aleatorio()
	print("Usuario: {:>30}\nEmail: {:>30}\nIdade: {:>30}".format(usuario['nome'],\
													usuario['email'],
													usuario['idade']))
