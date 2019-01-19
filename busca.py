from classes import No
from queue import PriorityQueue


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
        for acao in problema.acoes(no.estado):
            filho = No(acao, no)
            if filho not in borda:
                if problema.test_objetivo(filho.estado):
                    return solucao(filho)
                borda.append(filho)
    return None

# Busca em profundidade com lista de visitados

def DFSV(problema):
    no = No(problema.inicio)
    if problema.test_objetivo(no.estado):
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

# Busca por profundidade limitada
def DLS(problema, limite):
    no = No(problema.inicio)
    return DLSrecursiva(no, problema, limite)

def DLSrecursiva(no, problema, limite):
    if problema.test_objetivo(no.estado):
        return solucao(no.estado)
    elif limite == 0:
        return "termino"
    else:
        termino_ocorreu = False
        for acao in problema.acoes(no.estado):
            filho = No(acao, no)
            resultado = DLSrecursiva(filho, problema, limite-1)
            if resultado == "termino":
                termino_ocorreu = True
            elif resultado:
                return resultado
            if termino_ocorreu:
                return "termino"
            else:
                return False

# Busca de custo uniforme
def UCS(problema):
    no = No(problema.inicio)
    borda = PriorityQueue()
    borda.put((no.custo_caminho, no))
    explorado = set()

    while borda:
        aux = borda.get()
        no = aux[1]
        if problema.test_objetivo(no.estado):
            return solucao(no)
        explorado.add(no.estado)
        for acao in problema.acoes(no.estado):
            caminho_custo = int(problema.acao[acao][no.estado]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=caminho_custo)
            it = [i for i in borda.queue]
            if(filho.custo_caminho, filho) not in it and filho.estado not in explorado:
                borda.put((filho.custo_caminho, filho))

    return None