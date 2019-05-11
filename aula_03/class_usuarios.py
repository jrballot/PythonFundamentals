class User:
		def __init__(self, name, email, age):
			self.name = name
			self.email = email
			self.age = age

		def __str__(self):
			return 'Name: {}\nEmail: {}\nAge: {}'.format(self.name,self.email,self.age)

		def maioridade(self):
			if self.age >= 18:
				return True
			return False

		def maior_de_idade(self):
			if self.maioridade():
					return 'Permitido'
			else:
					return 'Requer mais de 18 anos'

class UserEnroller:
		def enroll_user(self):
			name = input('Enter your first name: ')
			email = input('Enter your email address: ')
			age = int(input('Enter you age: '))

			return User(name,email,age)

enroller = UserEnroller()

user_01 = enroller.enroll_user()

print(user_01)
print(user_01.maior_de_idade())
#user_01.maior_de_idade()
