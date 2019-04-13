
import aleatorio as foo
import json

def imprimir_bonito(obj):
	print(json.dumps(obj,indent=2))


def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = foo.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

lista_de_usuarios = gerar_lista_usuarios(100)

def gerar_csv(lista):
	TEMPLATE = "{};{};{}"

	print(TEMPLATE.format('NOME','EMAIL','IDADE'))
	for i in lista:
		print(TEMPLATE.format(i['nome'],i['email'],i['idade']))

#for usuario in lista_de_usuarios:
#	if usuario['idade'] > 30:
#		imprimir_bonito(usuario)

#for usuario in lista_de_usuarios:
#	if ('a' in usuario['email']) or ('d' in usuario['email']):
#		print("{};{};{}".format(usuario['nome'],usuario['email'], usuario['idade']))

nova_lista = [usuario for usuario in lista_de_usuarios \
					if ('a' in usuario['email'].lower()) or \
						('d' in usuario['email'].lower())]

gerar_csv(nova_lista)

