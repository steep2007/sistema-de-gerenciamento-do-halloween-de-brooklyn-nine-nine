from classes.estrategia import Estrategia
class Detetive:
    def __init__(self):
        self.__nome = None
        self.__sobrenome = None
        self.__cargo = None
        self.__participacaoAnterior = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSobrenome(self):
        return self.__sobrenome

    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getParticipacaoAnterior(self):
        return self.__participacaoAnterior

    def setParticipacaoAnterior(self, participacaoAnterior):
        self.__participacaoAnterior = participacaoAnterior
