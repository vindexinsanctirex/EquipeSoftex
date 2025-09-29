# CRUD com campos únicos - Versão Simples

'''Atalização
1. Adição do arquivo e função.
2. Bug com a variável id_counter no arquivo criar_registro.py na linha 56.
    - por algum motivo, o contador n está incrementando, embora crie sempre
        novos registros, porém, todos ficam com o Id = 1.
'''


from utils.sistema_crud import SistemaCRUD
from utils.funcoes import limpa_Tela, pausaTemporaria, telaCarregamento


sistema = SistemaCRUD()

while True:
    limpa_Tela()
    print("\n=== SISTEMA CRUD (OOP) ===")
    print("1. Criar registro")
    print("2. Listar registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("5. Sair")

    opcao = input("\n>> ")

    if opcao == "1":
        try:
            nome = input("Nome: ")
            email = input("Email: ")
            cpf = input("CPF (apenas números): ")
            idade = input("Idade: ")
            sistema.criar_registro(nome, email, cpf, idade)
            print("\nRegistro criado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        pausaTemporaria()
    elif opcao == "2":
        limpa_Tela()
        registros = sistema.listar_registros()
        if not registros:
            print("Nenhum registro encontrado.")
        else:
            for r in registros:
                print(f"ID: {r.id}, Nome: {r.nome}, Email: {r.email}, CPF: {r.cpf}, Idade: {r.idade}")
        pausaTemporaria()
    elif opcao == "3":
        try:
            id_reg = int(input("ID do registro a atualizar: "))
            nome = input("Novo nome (deixe em branco para manter): ")
            email = input("Novo email (deixe em branco para manter): ")
            cpf = input("Novo CPF (deixe em branco para manter): ")
            idade = input("Nova idade (deixe em branco para manter): ")
            sistema.atualizar_registro(id_reg, nome or None, email or None, cpf or None, idade or None)
            print("Registro atualizado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        pausaTemporaria()
    elif opcao == "4":
        try:
            id_reg = int(input("ID do registro a deletar: "))
            sistema.deletar_registro(id_reg)
            print("Registro deletado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        pausaTemporaria()
    elif opcao == "5":
        print("\nSaindo...")
        telaCarregamento()
        exit()
    else:
        limpa_Tela()
        print(f'\nA opção "{opcao}" inválida! Tente novamente.')
        pausaTemporaria()
