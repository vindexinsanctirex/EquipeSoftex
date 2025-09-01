# UPDATE - Atualizar registro

#importando funções e bibliotecas
from .funcoes import limpa_Tela, pausaTemporaria

def atualizarRegistro(lista_dados):
    limpa_Tela()
    print("\n=== Atualizar Registro ===")
    try:
        id_alvo = int(input("ID do registro a atualizar: "))
        encontrado = False
            
        for registro in lista_dados:
            if registro['id'] == id_alvo:
                encontrado = True
                print(f"""Registro atual: Nome: {registro['nome']}, 
                Email: {registro['email']}, CPF: {registro['cpf']}, 
                Idade: {registro['idade']}""")
                    
                novo_nome = input("Novo nome (deixe em branco para manter): ")
                if novo_nome:
                    registro['nome'] = novo_nome
                    
                # Verificar email único na atualização
                novo_email = input("Novo email (deixe em branco para manter): ")
                if novo_email:
                    email_valido = True
                    for outro_registro in lista_dados:
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
                    for outro_registro in lista_dados:
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
                    
                print("\nRegistro atualizado com sucesso!")
                pausaTemporaria()
                break
            
        if not encontrado:
            print("Registro não encontrado.")
            pausaTemporaria()
                
    except ValueError:
        limpa_Tela()
        print("ID deve ser um número.")
        pausaTemporaria()