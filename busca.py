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

# Busca por aprofundamento iterativo
def IDS(problema):
    profundidade = 0
    while True:
        resultado = DLS(problema, profundidade)
        if resultado != "termino":
            return resultado
        profundidade = profundidade + 1
        
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

# Busca Bidirecional
def BS(problema):
    no1, final = No(problema.inicio), No(problema.objetivo)
    if problema.test_objetivo(no1.estado):
        return [no1.estado]
    borda1, borda2 = [], []
    explorado1, explorado2 = set(), set()

    borda1.append(no1)
    borda2.append(final)

    explorado1.add(no1.estado)
    explorado2.add(final.estado)

    while borda1 and borda2:
        no1, no2 = borda1.pop(0), borda2.pop(0)

        aux = verificarBordas(no1, borda2)
        if aux:
            no2 = trocarPais(aux)
            no2.pais = no1.pais
            return solucao(final)

        explorado1.add(no1.estado)
        explorado2.add(no2.estado)

        for acao in problema.acao(no1.estado):
            filho = No(acao, no1)

            if filho not in borda1 and filho.estado not in explorado1:
                borda1.append(filho)

        print("Borda 1:")
        print([i.estado for i in borda1])

        for acao in problema.acoes(no2.estado):
            filho = No(acao, no2)

            if filho not in borda2 and filho.estado not in explorado2:
                borda2.append(filho)

        print("Borda 2:")
        print([i.estado for i in borda2])
        print("")

    return None


def verificarBordas(no, borda):
    for i in borda:
        if i.estado == no.estado:
            return i

    return False


def trocarPais(no):
    nos = []
    i = no
    while i:
        nos.append(i)
        i = i.pais
    nos.reverse()

    nos[0].pais = None
    for i in range(len(nos)-1):
        nos[i].pais = nos[i+1]

    return nos[-1]


# Busca A*
def AS(problema, heuristica):
    no = No(problema.inicio)
    borda = PriorityQueue()
    borda.put((heuristica[no.estado], no))
    explorado = set()

    while borda:
        aux = borda.get()
        no = aux[1]
        if problema.test_objetivo(no.estado):
            return solucao(no)
        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            custo_caminho = int(problema.acao[acao][no.estado]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=custo_caminho)

            f_n = heuristica[filho.estado] + filho.custo_caminho
            it = [i for i in borda.queue]
            if (f_n, filho) not in it and filho.estado not in explorado:
                borda.put((f_n, filho))

    return None

# Busca pela melhor escolha
def GBFS(problema, heuristica):
    no = No(problema.inicio)
    borda = PriorityQueue()
    borda.put((heuristica[no.estado], no))
    explorado = set()

    while borda:
        aux = borda.get()
        no = aux[1]
        if problema.test_objetivo(no.estado):
            return solucao(no)
        explorado.add(no.estado)

        for acao in problema.acao(no.estado):
            custo_caminho = int(problema.acao[acao][no.estado]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=custo_caminho)

            it = [i for i in borda.queue]
            if (heuristica[filho.estado], filho) not in it and filho.estado not in explorado:
                borda.put((heuristica[filho.estado], filho))

    return None
