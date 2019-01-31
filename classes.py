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
        print("JAAJ")
        return tuple(estadoNo) == tuple(self.objetivo)

    def acoes(self,estadoNo):
        acoes = []
        x = self.inicio.index(0)
        i = int(x / 3)
        j = int(x % 3)
        acoes_possiveis = self.acoes_possiveis(i, j)

        for acao in acoes_possiveis:
            novo_estado = self.inicio.copy()
            if acao is 'U':
                novo_estado[x], novo_estado[x - 3] = novo_estado[x - 3], novo_estado[x]
            elif acao is 'D':
                novo_estado[x], novo_estado[x + 3] = novo_estado[x + 3], novo_estado[x]
            elif acao is 'L':
                novo_estado[x], novo_estado[x - 1] = novo_estado[x - 1], novo_estado[x]
            elif acao is 'R':
                novo_estado[x], novo_estado[x + 1] = novo_estado[x + 1], novo_estado[x]
            acoes.append(ProblemaPuzz(novo_estado, self, acao))
        return acoes

    @staticmethod
    def acoes_possiveis(i,j):
        acao_possivel = ['U', 'D', 'L', 'R']
        if i == 0:
            acao_possivel.remove('U')
        if i == 2:
            acao_possivel.remove('D')
        if j == 0:
            acao_possivel.remove('L')
        if j == 1:
            acao_possivel.remove('R')
        return acao_possivel

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

    # def solucao(self):
    #     return [no.acao for no in self.caminho()[1:]]

    # def caminho(self):
    #     no, caminho_volta = self, []
    #     while no:
    #         caminho_volta.append(no)
    #         no = no.pais
    #     return list(reversed(caminho_volta))

   # def no_filho(self, problema, acao):
      #  prox_estado =

   # def expandir(self, problema):


    def __repr__(self):
        return self.estado + ", " + self.acao

