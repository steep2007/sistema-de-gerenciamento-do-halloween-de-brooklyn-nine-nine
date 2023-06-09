from classes.detetive import Detetive

class Peca:
    def __init__(self):
        self.__detetiveResponsavel = None
        self.__descricaoPeca = None

    def getDetetiveResponsavel(self):
        return self.__detetiveResponsavel

    def setDetetiveResponsavel(self, detetiveResponsavel):
        self.__detetiveResponsavel = detetiveResponsavel

    def getDescricaoPeca(self):
        return self.__descricaoPeca

    def setDescricaoPeca(self, descricaoPeca):
        self.__descricaoPeca = descricaoPeca
