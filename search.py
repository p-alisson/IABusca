from classes import No
from Queue import PriorityQueue


# BREADTH-FIRST SEARCH
def BFS(problema):
    node = No(problema.inicio)
    if problema.test_objetivo(node.estado):
        return [node.estado]
    frontier = [node]
    explored = set()  # conjunto vazio

    while frontier:
        node = frontier.pop(0)  # FILA (remove o primeiro elemento [0])
        explored.add(node.estado)

        for acao in problema.acao(node.estado):
            filho = No(acao, node)

            if filho not in frontier and filho.estado not in explored:
                if problema.test_objetivo(filho.estado):
                    return solucao(filho)
                frontier.append(filho)

    return None


# Print solucao
def solucao(no):
    lista = []
    while no:
        lista.append(no.estado)
        no = no.pais
    lista.reverse()
    return lista
