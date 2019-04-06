lista_usuarios = []

while True:
    opcao = input("""Menu: 
        1 Cadastrar usuario 
        2 Listar usuario 
        3 Buscar e deletar usuario 
        4 Sair
        : """)

    if opcao == '1':
        usuario = {
                'nome':input("Entre com nome do usuario: "),
                'idade': input("Entre com a idade do usuario: "),
                'email':input("Entre com o email do usuario: ")
        }
        lista_usuarios.append(usuario)

    elif opcao == '2':
        for i in lista_usuarios:
            print(i['nome'])
    
    elif opcao == '3':
        busca = input("Nome do usuario para buscar e deletar: ")
        for i in lista_usuarios:
            if i['nome'] == busca:
                print('Usuario encontrado, deletando...')
                lista_usuarios.remove(i)
    
    elif opcao == '4':
        exit()
    
    else:
        print("Escolha uma opcao")
