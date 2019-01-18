from classes import No
from Queue import PriorityQueue


def solucao(no):
    lista = []
    while no:
        lista.append(no.estado)
        no = no.pais
    lista.reverse()
    return lista

# Busca em Largura
def BFS(problema):
    no = No(problema.inicio)
    if problema.test_objetivo(no.estado):
        return [no.estado]
    borda = [no]
    explorado = set()

    while borda:
        no = borda.pop(0)
        explorado.add(no.estado)
        for acao in problema.acoes(no.estado):
            filho = No(acao, no)
            if filho not in borda and filho.estado not in explorado:
                if problema.test_objetivo(filho.estado):
                    return solucao(filho)
                borda.append(filho)
    return None

# Busca em profundidade
def DFS(problema):
    no = No(problema.inicio)
    if problema.test_objetivo(no.estado):
        return [no.estado]
    borda = [no]

    while borda:
        no = borda.pop(-1)
        for acao in problema.acoes(no.estado)
            filho = No(acao, no)
            if filho not in borda:
                if problema.test_objetivo(filho.estado)
                    return solucao(filho)
                borda.append(filho)
    return None

# Busca em profundidade com lista de visitados

def DFSV(problema):
    no = No(problema.inicio)
    if problema.test_objetivo(no.estdo):
        return [no.estado]
    borda = []
    explorado = set()
    borda.append(no)

    while borda:
        no = borda.pop(-1)
        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            filho = No(acao, no)

            if filho.estado not in explorado and filho not in borda:
                if problema.test_objetivo(filho.estado):
                    return solucao(filho)
                if filho.estado not in explorado:
                    borda.append(filho)
    return None


