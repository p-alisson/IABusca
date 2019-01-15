class Problema(object):

    def __init__(self, inicio, objetivo=None, acao=None):
        self.inicio = inicio
        self.objetivo = objetivo
        self.acao = acao

    def test_objetivo(self, estadoNo):
        return estadoNo == self.objetivo

    def acoes(self,estadoNo):
        return list(self.acao[estadoNo])


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

