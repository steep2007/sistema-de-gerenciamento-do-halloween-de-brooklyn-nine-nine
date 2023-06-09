from classes.detetive import Detetive

class Alianca:
    def __init__(self):
        self.__detetivesAliados = []

    def getDetetivesAliados(self):
        return self.__detetivesAliados

    def setDetetivesAliados(self, detetivesAliados):
        self.__detetivesAliados.append(detetivesAliados)
