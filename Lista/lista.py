# CRUD usando apenas listas - Versão Bruta
dados = []
id_counter = 1

while True:
    print("\n=== SISTEMA CRUD SIMPLES ===")
    print("1. Criar registro")
    print("2. Listar registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # CREATE - Criar registro
    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        idade = input("Idade: ")
        
        novo_registro = [id_counter, nome, email, idade]
        dados.append(novo_registro)
        print(f"Registro criado com ID: {id_counter}")
        id_counter += 1
    
    # READ - Listar registros
    elif opcao == "2":
        if not dados:
            print("Nenhum registro encontrado.")
        else:
            print("\n=== LISTA DE REGISTROS ===")
            for registro in dados:
                print(f"ID: {registro[0]}, Nome: {registro[1]}, Email: {registro[2]}, Idade: {registro[3]}")
    
    # UPDATE - Atualizar registro
    elif opcao == "3":
        try:
            id_alvo = int(input("ID do registro a atualizar: "))
            encontrado = False
            
            for i in range(len(dados)):
                if dados[i][0] == id_alvo:
                    encontrado = True
                    print(f"Registro atual: Nome: {dados[i][1]}, Email: {dados[i][2]}, Idade: {dados[i][3]}")
                    
                    novo_nome = input("Novo nome (deixe em branco para manter): ")
                    novo_email = input("Novo email (deixe em branco para manter): ")
                    nova_idade = input("Nova idade (deixe em branco para manter): ")
                    
                    if novo_nome:
                        dados[i][1] = novo_nome
                    if novo_email:
                        dados[i][2] = novo_email
                    if nova_idade:
                        dados[i][3] = nova_idade
                    
                    print("Registro atualizado com sucesso!")
                    break
            
            if not encontrado:
                print("Registro não encontrado.")
                
        except ValueError:
            print("ID deve ser um número.")
    
    # DELETE - Deletar registro
    elif opcao == "4":
        try:
            id_alvo = int(input("ID do registro a deletar: "))
            encontrado = False
            
            for i in range(len(dados)):
                if dados[i][0] == id_alvo:
                    encontrado = True
                    dados.pop(i)
                    print("Registro deletado com sucesso!")
                    break
            
            if not encontrado:
                print("Registro não encontrado.")
                
        except ValueError:
            print("ID deve ser um número.")
    
    # SAIR
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")