class Estrategia:
    def __init__(self):
        self.__detetive = None
        self.__listaAcoes = []

    def getDetetive(self):
        return self.__detetive

    def setDetetive(self, detetive):
        self.__detetive = detetive

    def getListaAcoes(self):
        return self.__listaAcoes

    def setListaAcoes(self, listaAcoes):
        self.__listaAcoes = listaAcoes