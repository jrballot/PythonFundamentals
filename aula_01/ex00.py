lista_usuarios = []
for i in range(3):
    usuario = {
            'nome':input("Entre com nome do usuario {}: ".format(i)),
            'idade': input("Entre com a idade do usuario {}: ".format(i)),
            'email':input("Entre com o email do usuario {}: ".format(i))
    }
    lista_usuarios.append(usuario)


for i in lista_usuarios:
    print(i['nome'])
        
    
