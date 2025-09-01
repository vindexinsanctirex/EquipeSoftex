# Aqui estão algumas funções de código recorrente.

import time, platform, os

#Função de limpa a tela. Independente do SO.
def limpa_Tela():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

#serve apenas pra o usuário ter noção e controle do q está na tela.
def pausaTemporaria():
    time.sleep(2)
    input("\nClique qualquer tecla para contiuar")

#Função de Tela de Carregamento.
def telaCarregamento():
    for i in range(6):
        print("o", end=" ", flush=True)
        time.sleep(0.25)