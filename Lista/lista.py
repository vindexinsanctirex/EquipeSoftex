# CRUD com campos únicos - Versão Simples
dados = []
id_counter = 1

while True:
    print("\n=== SISTEMA CRUD ===")
    print("1. Criar registro")
    print("2. Listar registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # CREATE - Criar registro
    if opcao == "1":
        nome = input("Nome: ")
        
        # Verificar email único
        while True:
            email = input("Email: ")
            email_repetido = False
            if "@" not in email or "." not in email:
                print("Email inválido! Tente novamente.")
                continue
            for registro in dados:
                if registro['email'].lower() == email.lower():
                    email_repetido = True
                    break
            
            if email_repetido:
                print("Email já cadastrado! Use outro.")
            else:
                break
        
        # Verificar CPF único
        while True:
            cpf = input("CPF(apenas números): ")
            cpf_repetido = False
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido! Deve conter 11 números.")
                continue
            for registro in dados:
                if 'cpf' in registro and registro['cpf'] == cpf:
                    cpf_repetido = True
                    break
            
            if cpf_repetido:
                print("CPF já cadastrado! Use outro.")
            else:
                break
        
        idade = input("Idade: ")
        
        novo_registro = {
            'id': id_counter,
            'nome': nome,
            'email': email,
            'cpf': cpf,
            'idade': idade
        }
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
                print(f"ID: {registro['id']}, Nome: {registro['nome']}, Email: {registro['email']}, CPF: {registro['cpf']}, Idade: {registro['idade']}")
    
    # UPDATE - Atualizar registro
    elif opcao == "3":
        try:
            id_alvo = int(input("ID do registro a atualizar: "))
            encontrado = False
            
            for registro in dados:
                if registro['id'] == id_alvo:
                    encontrado = True
                    print(f"Registro atual: Nome: {registro['nome']}, Email: {registro['email']}, CPF: {registro['cpf']}, Idade: {registro['idade']}")
                    
                    novo_nome = input("Novo nome (deixe em branco para manter): ")
                    if novo_nome:
                        registro['nome'] = novo_nome
                    
                    # Verificar email único na atualização
                    novo_email = input("Novo email (deixe em branco para manter): ")
                    if novo_email:
                        email_valido = True
                        for outro_registro in dados:
                            if outro_registro['id'] != id_alvo and outro_registro['email'].lower() == novo_email.lower():
                                email_valido = False
                                break
                        
                        if email_valido:
                            registro['email'] = novo_email
                        else:
                            print("Email já cadastrado em outro registro!")
                    
                    # Verificar CPF único na atualização
                    novo_cpf = input("Novo CPF (deixe em branco para manter): ")
                    if novo_cpf:
                        cpf_valido = True
                        for outro_registro in dados:
                            if outro_registro['id'] != id_alvo and outro_registro.get('cpf') == novo_cpf:
                                cpf_valido = False
                                break
                        
                        if cpf_valido:
                            registro['cpf'] = novo_cpf
                        else:
                            print("CPF já cadastrado em outro registro!")
                    
                    nova_idade = input("Nova idade (deixe em branco para manter): ")
                    if nova_idade:
                        registro['idade'] = nova_idade
                    
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
            
            for i, registro in enumerate(dados):
                if registro['id'] == id_alvo:
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