class Problema(object):

    def __init__(self, inicio, objetivo=None, acao=None):
        self.inicio = inicio
        self.objetivo = objetivo
        self.acao = acao

    def test_objetivo(self, estadoNo):
        return estadoNo == self.objetivo

    def acoes(self,estadoNo):
        return list(self.acao[estadoNo])

class ProblemaPuzz(Problema):

    def __init__(self, inicio, objetivo=None, acao=None):
        super().__init__(inicio, objetivo, acao)

    def test_objetivo(self, estadoNo):
        print("AIAIAI")
        return estadoNo == self.objetivo

class No(object):
    def __init__(self, estado, pais=None, acao=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pais = pais
        if pais:
            self.acao = pais.estado + "->" + estado
        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0
        if pais:
            self.profundidade = pais.profundidade + 1

    def __repr__(self):
        return self.estado + ", " + self.acao

class NoPuzz(object):
    def __init__(self, estado, pais=None, acao=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pais = pais
        self.acao = acao
        # if pais:
        #     self.acao = pais.estado + "->" + estado
        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0
        if pais:
            self.profundidade = pais.profundidade + 1

    def gera_filhos(self):
        filhos = []
        x = self.estado.index(0)
        # i = int(x / 3)
        # j = int(x % 3)
        acoes_possiveis = self.acoes_possiveis(x)

        for acao in acoes_possiveis:
            novo_estado = self.estado.copy()
            if acao is 'U':
                novo_estado[x], novo_estado[x - 3] = novo_estado[x - 3], novo_estado[x]
            elif acao is 'D':
                novo_estado[x], novo_estado[x + 3] = novo_estado[x + 3], novo_estado[x]
            elif acao is 'L':
                novo_estado[x], novo_estado[x - 1] = novo_estado[x - 1], novo_estado[x]
            elif acao is 'R':
                novo_estado[x], novo_estado[x + 1] = novo_estado[x + 1], novo_estado[x]
            filhos.append(NoPuzz(novo_estado, self, acao))

        return filhos

    def acoes_possiveis(self, x):
        acao_possivel = ['U', 'D', 'L', 'R']
        if x % 3 == 0:
            acao_possivel.remove('L')
        if x < 3:
            acao_possivel.remove('U')
        if x % 3 == 2:
            acao_possivel.remove('R')
        if x > 5:
            acao_possivel.remove('D')
        return acao_possivel


    def __str__(self):
        return str(self.estado[0:3]) + '\n' + str(self.estado[3:6]) + '\n' + str(self.estado[6:9])
