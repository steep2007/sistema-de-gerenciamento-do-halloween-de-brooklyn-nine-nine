class Regras:
    def __init__(self):
        self.__restricoesLocal = None
        self.__duracao = None

    def getRestricoesLocal(self):
        return self.__restricoesLocal

    def setRestricoesLocal(self, restricoesLocal):
        self.__restricoesLocal = restricoesLocal

    def getDuracao(self):
        return self.__duracao

    def setDuracao(self, duracao):
        self.__duracao = duracao