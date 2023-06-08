import mysql.connector

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

class Alianca:
    def __init__(self):
        self.__detetivesAliados = []

    def getDetetivesAliados(self):
        return self.__detetivesAliados

    def setDetetivesAliados(self, detetivesAliados):
        self.__detetivesAliados.append(detetivesAliados)

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

    def setListaAcoes(self, acao):
        self.__listaAcoes.append(acao)

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

class Ranking:
    def __init__(self):
        self.__listaDetetives = []
        self.__pontuacoes = None

    def getListaDetetives(self):
        return self.__listaDetetives

    def setListaDetetives(self, listaDetetives):
        self.__listaDetetives.append(listaDetetives)

    def getPontuacoes(self):
        return self.__pontuacoes

    def setPontuacoes(self, pontuacoes):
        self.__pontuacoes = pontuacoes

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

detetive1 = Detetive()
detetive1.setNome("Jake")
detetive1.setSobrenome("Peralta")
detetive1.setCargo("Detetive de Homicídios")
detetive1.setParticipacaoAnterior("Perdedor")
print("Detetive 1")
print("Nome: {}".format(detetive1.getNome()))
print("Sobrenome: {}".format(detetive1.getSobrenome()))
print("Cargo: {}".format(detetive1.getCargo()))
print("Participação Anterior: {}".format(detetive1.getParticipacaoAnterior()))
print()

detetive2 = Detetive()
detetive2.setNome("Amy")
detetive2.setSobrenome("Santiago")
detetive2.setCargo("Detetive de Homicídios")
detetive2.setParticipacaoAnterior("Perdedor")
print("Detetive 2")
print("Nome: {}".format(detetive2.getNome()))
print("Sobrenome: {}".format(detetive2.getSobrenome()))
print("Cargo: {}".format(detetive2.getCargo()))
print("Participação Anterior: {}".format(detetive2.getParticipacaoAnterior()))
print()

detetive3 = Detetive()
detetive3.setNome("Rosa")
detetive3.setSobrenome("Diaz")
detetive3.setCargo("Detetive de Homicídios")
detetive3.setParticipacaoAnterior("Perdedor")
print("Detetive 3")
print("Nome: {}".format(detetive3.getNome()))
print("Sobrenome: {}".format(detetive3.getSobrenome()))
print("Cargo: {}".format(detetive3.getCargo()))
print("Participação Anterior: {}".format(detetive3.getParticipacaoAnterior()))
print()

detetive4 = Detetive()
detetive4.setNome("Terry")
detetive4.setSobrenome("Jeffords")
detetive4.setCargo("Sargento de Polícia")
detetive4.setParticipacaoAnterior("Perdedor")
print("Detetive 4")
print("Nome: {}".format(detetive4.getNome()))
print("Sobrenome: {}".format(detetive4.getSobrenome()))
print("Cargo: {}".format(detetive4.getCargo()))
print("Participação Anterior: {}".format(detetive4.getParticipacaoAnterior()))
print()

detetive5 = Detetive()
detetive5.setNome("Charles")
detetive5.setSobrenome("Boyle")
detetive5.setCargo("Detetive de Homicídios")
detetive5.setParticipacaoAnterior("Perdedor")
print("Detetive 5")
print("Nome: {}".format(detetive5.getNome()))
print("Sobrenome: {}".format(detetive5.getSobrenome()))
print("Cargo: {}".format(detetive5.getCargo()))
print("Participação Anterior: {}".format(detetive5.getParticipacaoAnterior()))
print()

detetive6 = Detetive()
detetive6.setNome("Raymond")
detetive6.setSobrenome("Holt")
detetive6.setCargo("Capitão de Polícia")
detetive6.setParticipacaoAnterior("Vencedor")
print("Detetive 6")
print("Nome: {}".format(detetive6.getNome()))
print("Sobrenome: {}".format(detetive6.getSobrenome()))
print("Cargo: {}".format(detetive6.getCargo()))
print("Participação Anterior: {}".format(detetive6.getParticipacaoAnterior()))
print()

alianca1 = Alianca()
alianca1.setDetetivesAliados(detetive6)
alianca1.setDetetivesAliados(detetive2)
print("Aliança 1")
print(f"Detetives Aliados: {detetive6.getNome()} e {detetive2.getNome()}")
print()

alianca2 = Alianca()
alianca2.setDetetivesAliados(detetive1)
alianca2.setDetetivesAliados(detetive5)
print("Aliança 2")
print(f"Detetives Aliados: {detetive1.getNome()} e {detetive5.getNome()}")
print()

alianca3 = Alianca()
alianca3.setDetetivesAliados(detetive1)
alianca3.setDetetivesAliados(detetive4)
print("Aliança 3")
print(f"Detetives Aliados: {detetive1.getNome()} e {detetive4.getNome()}")
print()


