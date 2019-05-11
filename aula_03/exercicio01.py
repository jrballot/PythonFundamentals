user = {
	'name':'Lucas',
	'email':'lucas.salles@4linux.com.br',
	'age': 25
}

class User:
		def __init__(self, name, email, age):
				self.name = name
				self.email = email
				self.age = age


		def __str__(self):
				return 'Nome: {}; Email: {}; Idade: {}'.format(self.name,self.email,self.age)

obj_user = User(
	'Julio',
	'julio.ballot@4linux.com.br',
	25
)

print(obj_user)

class Lampada:
		def __init__(self,estado='apagado'):
				self.estado = estado

		def esta_apagada(self):
				if self.estado == 'apagado':
						return  True
				return False

		def pressionar_interruptor(self):
				if self.esta_apagada():
						self.estado = 'aceso'
				else:
						self.estado = 'apagado'

		def __str__(self):
				return 'Estado: {} !!!'.format(self.estado)

lampada_1 = Lampada()
lampada_2 = Lampada('aceso')


print('Lampada 01')
print(lampada_1)
print('Lampada 02')
print(lampada_2)
