# DELETE - Deletar registro.

from .funcoes import limpa_Tela, pausaTemporaria

def deletarRegistro(lista_dados):
    limpa_Tela()
    print("\n=== Deletar Registro ===")
    try:
        id_alvo = int(input("ID do registro a deletar: "))
        encontrado = False
            
        for i, registro in enumerate(lista_dados):
            if registro['id'] == id_alvo:
                encontrado = True
                lista_dados.pop(i)
                limpa_Tela()
                print("\nRegistro deletado com sucesso!")
                pausaTemporaria()
                break
            
        if not encontrado:
            print("Registro não encontrado.")
            pausaTemporaria()
                
    except ValueError:
        print("ID deve ser um número.")
        pausaTemporaria()