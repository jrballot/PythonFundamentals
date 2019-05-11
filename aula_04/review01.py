
def par(numero):
    if numero % 2 == 0:
        return True
    return False

def gerar_lista(numero):
	return [ i + 1 for i in range(numero) if par(i)]


lista_numeros_pares  = gerar_lista(5)
for numero in lista_numeros_pares:
    if not par(numero):
        raise Exception('{} nao e um numero par'.format(numero))
    
print(lista_numeros_pares)
