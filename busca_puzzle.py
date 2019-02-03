from classes import No, NoPuzz
from queue import PriorityQueue

def solucaoPuzz(no):
    solucao = []
    solucao.append(no.estado)
    path = no
    while path.pais:
        path = path.pais
        solucao.append(path.estado)
    solucao = solucao[:-1]
    solucao.reverse()
    return solucao

def BFSPuzz(problema):
    no_inicio = NoPuzz(problema.inicio)
    if problema.test_objetivo(no_inicio.estado):
        return solucaoPuzz(no_inicio)
    borda = [no_inicio]
    explorado = []

    while borda:
        no = borda.pop(0)
        explorado.append(no.estado)
        filhos = no.gera_filhos()
        for filho in filhos:
            if filho.estado not in explorado:
                if problema.test_objetivo(filho.estado):
                    return solucaoPuzz(filho)
                borda.append(filho)
    return None

# Busca em profundidade
def DFSPuzz(problema):
    no_inicio = NoPuzz(problema.inicio)
    if problema.test_objetivo(no_inicio.estado):
        return solucaoPuzz(no_inicio)
    borda = [no_inicio]

    while borda:
        no = borda.pop(-1)
        filhos = no.gera_filhos()
        for filho in filhos:
            if filho not in borda:
                if problema.test_objetivo(filho.estado):
                    return solucaoPuzz(filho)
                borda.append(filho)
    return None

# Busca em profundidade com lista de visitados
def DFSVPuzz(problema):
    no_inicio = NoPuzz(problema.inicio)
    if problema.test_objetivo(no_inicio.estado):
        return solucaoPuzz(no_inicio)
    borda = [no_inicio]
    explorado = []

    while borda:
        no = borda.pop(-1)
        explorado.append(no.estado)
        filhos = no.gera_filhos()
        for filho in filhos:
            if filho.estado not in explorado and filho not in borda:
                if problema.test_objetivo(filho.estado):
                    return solucaoPuzz(filho)
                # if filho.estado not in explorado:
                borda.append(filho)
    return None