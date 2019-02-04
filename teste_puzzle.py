import os

from busca import DLS
from busca_puzzle import Astar, BFSPuzz, DFSPuzz, DFSVPuzz
from classes import ProblemaPuzz

QTD_ITERACOES = 20
INICIO = [0, 8, 4,
          1, 6, 3,
          7, 5, 2]
OBJETIVO = [0,1,2,
            3,4,5,
            6,7,8]
# OBJETIVO = [1,2,3,8,0,4,7,6,5]

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
        print(BFSPuzz(problema))

    elif opt == 2:
        print("BUSCA EM PROFUNDIDADE LIMITADA:")
        print(DLS(problema, QTD_ITERACOES))

    elif opt == 3:
        print("BUSCA EM PROFUNDIDADE ITERATIVA:")
        print(Astar(problema))

    elif opt == 4:
        print("BUSCA EM PROFUNDIDADE:")
        print(DFSPuzz(problema))

    elif opt == 5:
        print("BUSCA EM PROFUNDIDADE COM VISITADOS:")
        print(DFSVPuzz(problema))


    elif opt == 0:
        return opt

    else:
        print("OPÇÃO INVÁLIDA!")

    return 1


option = 1
while option:
    problema = ProblemaPuzz(INICIO, OBJETIVO)
    option = menu(problema)