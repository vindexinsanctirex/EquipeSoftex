# CRUD com campos únicos - Versão Simples

'''Atalização
1. Adição do arquivo e função.
2. Bug com a variável id_counter no arquivo criar_registro.py na linha 56.
    - por algum motivo, o contador n está incrementando, embora crie sempre
        novos registros, porém, todos ficam com o Id = 1.
'''

#Importando todos os arquivos para a função main.
from utils.criar_registro import criandoRegistro
from utils.listar_registros import listandoRegistros
from utils.deletar_registro import deletarRegistro
from utils.atualizar_registro import atualizarRegistro
from utils.funcoes import limpa_Tela, pausaTemporaria, telaCarregamento

#biblioteca a parte.
import time

dados = []
id_counter = 1

while True:
    limpa_Tela()
    print("\n=== SISTEMA CRUD ===")
    print("1. Criar registro")
    print("2. Listar registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("5. Sair")
    
    opcao = input("\n>> ")
    
    match opcao:
        # CREATE - Criar registro
        case "1":
            id_counter=criandoRegistro(dados, id_counter)
            
        # READ - Listar registros
        case "2":
            listandoRegistros(dados)

        # UPDATE - Atualizar registro
        case "3":
            atualizarRegistro(dados)

        # DELETE - Deletar registro
        case "4":
            deletarRegistro(dados)

        # SAIR
        case "5":
            print("\nSaindo...")
            #Apenas uma adição visual | O código está em funcoes.py
            telaCarregamento()
            exit()
        
        case _:
            limpa_Tela()   #Add visual | funcoes.py
            print(f'\nA opção "{opcao}" inválida! Tente novamente.')
            pausaTemporaria()
                