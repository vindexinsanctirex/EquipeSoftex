#Função CREATE - Criando Registros.

from .funcoes import limpa_Tela, pausaTemporaria

def criandoRegistro(lista_dados, id_count):
    limpa_Tela()
    print("\n===Criando Registro===")
    nome = input("Nome: ")
            
    # Verificar email único
    while True:
        email = input("Email: ")
        email_repetido = False
        if "@" not in email or "." not in email:
            print("Email inválido! Tente novamente.")
            continue
        for registro in lista_dados:
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
            for registro in lista_dados:
                if 'cpf' in registro and registro['cpf'] == cpf:
                    cpf_repetido = True
                    break
                
            if cpf_repetido:
                print("CPF já cadastrado! Use outro.")
            else:
                break
            
        idade = input("Idade: ")
            
        novo_registro = {
            'id': id_count,
            'nome': nome,
            'email': email,
            'cpf': cpf,
            'idade': idade
        }
        lista_dados.append(novo_registro)
        print(f"\nRegistro criado com ID: {id_count}")
        id_count += 1     #provavel bug no contador.
        pausaTemporaria()     
        return id_count