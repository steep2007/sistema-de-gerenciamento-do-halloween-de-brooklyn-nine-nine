from classes.detetive import Detetive

class Competicao:
    def __init__(self):
        self.__listaParticipantes = []
        self.__dataCompeticao = None

    def getListaParticipantes(self):
        return self.__listaParticipantes

    def setListaParticipantes(self, listaParticipantes):
        self.__listaParticipantes.append(listaParticipantes)

    def getDataCompeticao(self):
        return self.__dataCompeticao

    def setDataCompeticao(self, dataCompeticao):
        self.__dataCompeticao = dataCompeticao