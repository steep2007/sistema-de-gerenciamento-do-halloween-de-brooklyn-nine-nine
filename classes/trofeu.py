from classes.detetive import Detetive

class Trofeu:
    def __init__(self):
        self.__detetiveVencedor = None
        self.__anoVitoria = None
        self.__fraseVitoria = None

    def getDetetiveVencedor(self):
        return self.__detetiveVencedor

    def setDetetiveVencedor(self, detetiveVencedor):
        self.__detetiveVencedor = detetiveVencedor

    def getAnoVitoria(self):
        return self.__anoVitoria

    def setAnoVitoria(self, anoVitoria):
        self.__anoVitoria = anoVitoria

    def getFraseVitoria(self):
        return self.__fraseVitoria

    def setFraseVitoria(self, fraseVitoria):
        self.__fraseVitoria = fraseVitoria