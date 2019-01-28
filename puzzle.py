from classes import Problema, No
from busca import *

class EightPuzzle(Problema):

    def __init__(self, inicio, objetivo=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.objetivo = objetivo
        Problema.__init__(self, inicio, objetivo)

    def acha_zero(self, estado):

        return estado.index(0)

    def acoes(self, estado):

        acoes_possiveis = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        indice_zero = self.acha_zero(estado)

        if indice_zero % 3 == 0:
            acoes_possiveis.remove('LEFT')
        if indice_zero < 3:
            acoes_possiveis.remove('UP')
        if indice_zero % 3 == 2:
            acoes_possiveis.remove('RIGHT')
        if indice_zero > 5:
            acoes_possiveis.remove('DOWN')

        return list(acoes_possiveis)

    def resultado(self, estado, acao):

        zero = self.acha_zero(estado)
        novo_estado = list(estado)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = zero + delta[acao]
        novo_estado[zero], novo_estado[neighbor] = novo_estado[neighbor], novo_estado[zero]

        return tuple(novo_estado)

    def test_objetivo(self, estado):

        return estado == self.objetivo

    def possivel_resolver(self, estado):

        inversao = 0
        for i in range(len(estado)):
            for j in range(i + 1, len(estado)):
                if (estado[i] > estado[j]) and estado[i] != 0 and estado[j] != 0:
                    inversao += 1

        return inversao % 2 == 0

    def h(self, no):
        return sum(s != g for (s, g) in zip(no.estado, self.objetivo))


puzz = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))
# print(AS(puzz, puzz.h(No((1, 2, 3, 4, 5, 6, 0, 7, 8)))))
print(DFSV(puzz))