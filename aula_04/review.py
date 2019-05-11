# revisao rapida
# escrever uma funcao que recebe 
# um numero inteiro e retorn uma lista 
# com todos os numeros menores ou iguais a esse menos o zero
# ex: gerar_lista(5) -> [1,2,3,4,5]

def ret_list_map(numero):
	return [ i + 1 for i in range(numero)]

def ret_int(a):
	lista = []
	for i in range(a):
		lista.append(i+1)
	return lista

gerar_lista = lambda n: [i + 1 for i in range(n)]
print(gerar_lista(20))

gerar_lista = ret_list_map(10)
print(gerar_lista)

gerar_lista = ret_int(5)
print(gerar_lista)


