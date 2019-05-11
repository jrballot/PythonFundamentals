variavel = 5
variabel = 5 + 5

def soma(a,b):
		return a + b

variabel = soma(5,5)

apelido = soma
variabel = apelido(2,2)

resultado_bool = variabel < 10

if resultado_bool:
		print('Entre 5 e 10')
elif variabel < 5:
		print('Menor do que 5')
else:
		print('Maior do que 10')

lista_de_numeros = [1,2,3,4,5]
for numero in lista_de_numeros:
		print(numero)

for letra in 'Julio Rangel Ballot':
		if letra == 'c' or letra == 'a':
				print(letra)

x = 0
while x < 10:
		print('Hello, world novamente')
		x = x + 1

try:
		idade = int(input('Digite a sua idade: '))
		print('Sua idade é {}'.format(idade))
except:
		print('Idade invalida')
finally:
		print('Sempre será executado')
