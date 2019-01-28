import os

from pip._vendor.distlib.compat import raw_input

from busca import BFS, DFS, DFSV, IDS, DLS, UCS, GBFS, AS, BS
from classes import Problema
from mundos import map_romania, HSLD

QTD_ITERACOES = 20
INICIO_MAP = "Oradea"
OBJETIVO_MAP = "Bucharest"

def menu(problema):
    print("1: BUSCA EM LARGURA:")
    print("2: BUSCA EM PROFUNDIDADE LIMITADA:")
    print("3: BUSCA EM PROFUNDIDADE ITERATIVA:")
    print("4: BUSCA EM PROFUNDIDADE:")
    print("5: BUSCA EM PROFUNDIDADE COM VISITADOS:")
    print("6: BUSCA DE CUSTO UNIFORME:")
    print("7: BUSCA GULOSA:")
    print("8: BUSCA A*:")
    print("9: BUSCA BIDIRECIONAL:")
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
    elif opt == 6:
        print("BUSCA CUSTO UNIFORME")
        print(UCS(problema))

    elif opt == 7:
        print("BUSCA GULOSA")
        print(GBFS(problema, HSLD))

    elif opt == 8:
        print("BUSCA A*")
        print(AS(problema, HSLD))

    elif opt == 9:
        print("BUSCA BIDIRECIONAL:")
        print(BS(problema))


    elif opt == 0:
        return opt

    else:
        print("OPÇÃO INVÁLIDA!")

    return 1


option = 1
while option:
    problema = Problema(INICIO_MAP, OBJETIVO_MAP, map_romania)
    option = menu(problema)

print("Você saiu ^^ ")
