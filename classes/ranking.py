from classes.detetive import Detetive

class Ranking:
    def __init__(self):
        self.__listaDetetives = []
        self.__pontuacoes = []

    def getListaDetetives(self):
        return self.__listaDetetives

    def setListaDetetives(self, listaDetetives):
        self.__listaDetetives.append(listaDetetives)

    def getPontuacoes(self):
        return self.__pontuacoes

    def setPontuacoes(self, pontuacoes):
        self.__pontuacoes.append(pontuacoes)