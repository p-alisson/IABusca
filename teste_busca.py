import os
from busca import BFS, DFS, DFSV, IDS, DLS, UCS, GBFS, AS, BS
from classes import Problema
from mundos import map_romania, HSLD
from mundos import vaccum_world as vaccum

NUMBER_OF_ITERATIONS = 20
INIT_MAP = "Oradea"
GOAL_MAP = "Bucharest"
INIT_VACCUM = "ESS"
GOAL_VACCUM = "DLL"


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
        print(BFS(problema[0]))
        print(BFS(problema[1]))

    elif opt == 2:
        print("BUSCA EM PROFUNDIDADE LIMITADA:")
        print(DLS(problema[0], NUMBER_OF_ITERATIONS))
        print(DLS(problema[1], NUMBER_OF_ITERATIONS))

    elif opt == 3:
        print("BUSCA EM PROFUNDIDADE ITERATIVA:")
        print(IDS(problema[0]))
        print(IDS(problema[1]))

    elif opt == 4:
        print("BUSCA EM PROFUNDIDADE:")
        print(DFS(problema[0]))
        print(DFS(problema[1]))

    elif opt == 5:
        print("BUSCA EM PROFUNDIDADE COM VISITADOS:")
        print(DFSV(problema[0]))
        print(DFSV(problema[1]))

    elif opt == 6:
        print("BUSCA CUSTO UNIFORME")
        a, b = raw_input("Início:\n"), raw_input("Objetivo:\n")
        print(UCS(Problema(a, b, map_romania)))

    elif opt == 7:
        print("BUSCA GULOSA")
        inicio = raw_input("Início:\n")
        p = Problema(inicio, "Bucharest", map_romania)
        print(GBFS(p, HSLD))

    elif opt == 8:
        print("BUSCA A*")
        inicio = raw_input("Início:\n")
        p = Problema(inicio, "Bucharest", map_romania)
        print(AS(p, HSLD))

    elif opt == 9:
        print("BUSCA BIDIRECIONAL:")
        a, b = raw_input("Início:\n"), raw_input("Objetivo:\n")
        print(BS(Problema(a, b, map_romania)))


    elif opt == 0:
        return opt

    else:
        print("OPÇÃO INVÁLIDA!")

    return 1


option = 1
while option:
    problema = [Problema(INIT_MAP, GOAL_MAP, map_romania),
                Problema(INIT_VACCUM, GOAL_VACCUM, vaccum)]
    option = menu(problema)

print("Você saiu ^^ ")
