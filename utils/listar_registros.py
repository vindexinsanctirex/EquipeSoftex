# READ - Listar registros

#importando funções e bibliotecas
from .funcoes import limpa_Tela, pausaTemporaria

def listandoRegistros(lista_dados):
    limpa_Tela()
    print("\n===Lista de Registros===")
    if not lista_dados:
        print("Nenhum registro encontrado.")
        pausaTemporaria()

    else:
        print("\n=== LISTA DE REGISTROS ===")
        for registro in lista_dados:
            print(f"""ID: {registro['id']}, 
                Nome: {registro['nome']}, 
                Email: {registro['email']}, 
                CPF: {registro['cpf']}, 
                Idade: {registro['idade']}""")
        pausaTemporaria()