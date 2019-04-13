import aleatorio

def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = aleatorio.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

lista_de_usuarios = gerar_lista_usuarios(10)

for usuario in lista_de_usuarios:
	print("Usuario: {:>30}\nEmail: {:>30}\nIdade: {:>30}".format(usuario['nome'],\
													usuario['email'],
													usuario['idade']))

print(__name__)
