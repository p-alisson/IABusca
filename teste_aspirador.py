import os

from busca import BFS, DFS, DFSV, IDS, DLS
from classes import Problema
from mundos import mundo_aspirador as aspirador

QTD_ITERACOES = 20
INICIO_ASPIRADOR = "ESS"
OBJETIVO_ASPIRADOR = "DLL"

def menu(problema):
    print("1: BUSCA EM LARGURA:")
    print("2: BUSCA EM PROFUNDIDADE LIMITADA:")
    print("3: BUSCA EM PROFUNDIDADE ITERATIVA:")
    print("4: BUSCA EM PROFUNDIDADE:")
    print("5: BUSCA EM PROFUNDIDADE COM VISITADOS:")
    print("0: SAIR")

    opt = int(input("Opção: "))

    os.system('cls' if os.name == 'nt' else 'clear')  # LIMPAR TERMINAL

    if opt == 1:
        print("BUSCA EM LARGURA:")
        print(BFS(problema))

    elif opt == 2:
        print("BUSCA EM PROFUNDIDADE LIMITADA:")
        print(DLS(problema, QTD_ITERACOES))

    elif opt == 3:
        print("BUSCA EM PROFUNDIDADE ITERATIVA:")
        print(IDS(problema))

    elif opt == 4:
        print("BUSCA EM PROFUNDIDADE:")
        print(DFS(problema))

    elif opt == 5:
        print("BUSCA EM PROFUNDIDADE COM VISITADOS:")
        print(DFSV(problema))


    elif opt == 0:
        return opt

    else:
        print("OPÇÃO INVÁLIDA!")

    return 1


option = 1
while option:
    problema = Problema(INICIO_ASPIRADOR, OBJETIVO_ASPIRADOR, aspirador)
    option = menu(problema)

print("Você saiu ^^ ")