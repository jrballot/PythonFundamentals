# Missão 1:
# Criar uma função 'cadastrar_usuario'
# que retorne um dicionário de usuário.
# O dicionário deve conter a propriedades:
# - nome
# - email
# - idade
# e os valores devem ser digitados 
# pelo usuário do através do terminal (input)

import datetime
import os
import time

usuarios = []

def cadastrar_usuarios():
	usuario = {
				'nome': input('Entre com nome do usuario: '),
				'idade': input('Entre com idade do usuario: '),
				'email': input('Entre com email do usuario: '),
				'data_cadastro': datetime.datetime.now()
			}
	usuarios.append(usuario)
	return usuarios
start_time = time.process_time()
os.system('clear')
usuario = cadastrar_usuarios()
print(usuario)

d = usuario[0]['data_cadastro']
print(d.strftime('%B %d, %Y       %c'))
end_time = time.process_time()

print("Operacao iniciada em {} e finalizada em {}\
		\nTotal de {} decoridos".format(start_time,end_time,end_time-start_time))

