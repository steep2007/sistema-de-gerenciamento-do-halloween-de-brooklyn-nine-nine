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

    def setListaAcoes(self, listaAcoes):
        self.__listaAcoes = listaAcoes

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
        self.__pontuacoes = []

    def getListaDetetives(self):
        return self.__listaDetetives

    def setListaDetetives(self, listaDetetives):
        self.__listaDetetives.append(listaDetetives)

    def getPontuacoes(self):
        return self.__pontuacoes

    def setPontuacoes(self, pontuacoes):
        self.__pontuacoes.append(pontuacoes)

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
print(f"Detetives Aliados: {alianca1.getDetetivesAliados()[0].getNome()} e {alianca1.getDetetivesAliados()[1].getNome()}")
print()

alianca2 = Alianca()
alianca2.setDetetivesAliados(detetive1)
alianca2.setDetetivesAliados(detetive5)
print("Aliança 2")
print(f"Detetives Aliados: {alianca2.getDetetivesAliados()[0].getNome()} e {alianca2.getDetetivesAliados()[1].getNome()}")
print()

alianca3 = Alianca()
alianca3.setDetetivesAliados(detetive1)
alianca3.setDetetivesAliados(detetive4)
print("Aliança 3")
print(f"Detetives Aliados: {alianca3.getDetetivesAliados()[0].getNome()} e {alianca3.getDetetivesAliados()[1].getNome()}")
print()

peca1 = Peca()
peca1.setDetetiveResponsavel(detetive1)
peca1.setDescricaoPeca("O Mistério da Máscara Desaparecida - Uma máscara valiosa desapareceu de um museu e os participantes devem investigar pistas, seguir suspeitos e descobrir quem é o responsável pelo roubo.")
print("Peça 1")
print(f"Detetive Responsável: {peca1.getDetetiveResponsavel().getNome()}")
print(f"Descrição da Peça: {peca1.getDescricaoPeca()}\n")

peca2 = Peca()
peca2.setDetetiveResponsavel(detetive2)
peca2.setDescricaoPeca("Espelhos Enganosos: Colocar espelhos estrategicamente posicionados para criar ilusões de ótica e confundir os detetives. Eles terão que superar as ilusões para encontrar pistas e resolver o roubo.")
print("Peça 2")
print(f"Detetive Responsável: {peca2.getDetetiveResponsavel().getNome()}")
print(f"Descrição da Peça: {peca2.getDescricaoPeca()}\n")

peca3 = Peca()
peca3.setDetetiveResponsavel(detetive3)
peca3.setDescricaoPeca("O Enigma do Fantasma do Armário na delegacia, um fantasma assombra o armário de evidências. Os participantes devem seguir as pistas e solucionar o enigma por trás do fantasma para acalmar os espíritos inquietos.")
print("Peça 3")
print(f"Detetive Responsável: {peca3.getDetetiveResponsavel().getNome()}")
print(f"Descrição da Peça: {peca3.getDescricaoPeca()}\n")

peca4 = Peca()
peca4.setDetetiveResponsavel(detetive4)
peca4.setDescricaoPeca("A Aventura do Tesouro Assombrado - Uma lenda local fala de um tesouro escondido em um local supostamente assombrado. Os participantes devem enfrentar seus medos, decifrar charadas e encontrar o tesouro enquanto desvendam os segredos sombrios que cercam o local.")
print("Peça 4")
print(f"Detetive Responsável: {peca4.getDetetiveResponsavel().getNome()}")
print(f"Descrição da Peça: {peca4.getDescricaoPeca()}\n")

estrategia1 = Estrategia()
estrategia1.setDetetive(detetive1)
estrategia1.setListaAcoes("Espalhe informações falsas ou crie situações enganosas para induzir os outros competidores a cometerem erros.")
print("Estratégia 1")
print(f'Detetive: {estrategia1.getDetetive().getNome()}')
print(f'Estratégia: {estrategia1.getListaAcoes()} \n')

estrategia2 = Estrategia()
estrategia2.setDetetive(detetive6)
estrategia2.setListaAcoes("Planeje um evento chamativo e divertido para desviar a atenção dos competidores, enquanto avançam nas tarefas.")
print("Estratégia 2")
print(f'Detetive: {estrategia2.getDetetive().getNome()}')
print(f'Estratégia: {estrategia2.getListaAcoes()} \n')

estrategia3 = Estrategia()
estrategia3.setDetetive(detetive2)
estrategia3.setListaAcoes("Planeje um evento chamativo e divertido para desviar a atenção dos competidores, enquanto avançam nas tarefas.")
print("Estratégia 3")
print(f'Detetive: {estrategia3.getDetetive().getNome()}')
print(f'Estratégia: {estrategia3.getListaAcoes()} \n')

estrategia4 = Estrategia()
estrategia4.setDetetive(detetive3)
estrategia4.setListaAcoes("Se disfarce como funcionários de um local específico para obter acesso privilegiado e informações valiosas que possam ajudá-lo.")
print("Estratégia 4")
print(f'Detetive: {estrategia4.getDetetive().getNome()}')
print(f'Estratégia: {estrategia4.getListaAcoes()} \n')

regras1 = Regras()
regras1.setRestricoesLocal("Deve ocorrer dentro do Museu")
regras1.setDuracao("A duração é de um dia inteiro")
print("Regras 1")
print("Restrições Locais: {}".format(regras1.getRestricoesLocal()))
print("Duração: {}\n".format(regras1.getDuracao()))

regras2 = Regras()
regras2.setRestricoesLocal("Deve ocorrer dentro da Galeria de Arte")
regras2.setDuracao("A duração é de algumas horas")
print("Regras 2")
print("Restrições Locais: {}".format(regras2.getRestricoesLocal()))
print("Duração: {}\n".format(regras2.getDuracao()))

regras3 = Regras()
regras3.setRestricoesLocal("Deve ocorrer dentro da Delegacia")
regras3.setDuracao("A duração é de algumas horas à noite")
print("Regras 3")
print("Restrições Locais: {}".format(regras3.getRestricoesLocal()))
print("Duração: {}\n".format(regras3.getDuracao()))

regras4 = Regras()
regras4.setRestricoesLocal("Deve ocorrer em um casa assombrado")
regras4.setDuracao("A duração é de algumas horas na madrugada")
print("Regras 4")
print("Restrições Locais: {}".format(regras4.getRestricoesLocal()))
print("Duração: {}\n".format(regras4.getDuracao()))

competicao1 = Competicao()
competicao1.setListaParticipantes(detetive1)
competicao1.setListaParticipantes(detetive2)
competicao1.setListaParticipantes(detetive3)
competicao1.setListaParticipantes(detetive4)
competicao1.setDataCompeticao("31/10/2016")
print("Competição 1")
print(f"Participantes: {competicao1.getListaParticipantes()[0].getNome()}, {competicao1.getListaParticipantes()[1].getNome()}, {competicao1.getListaParticipantes()[2].getNome()}, {competicao1.getListaParticipantes()[3].getNome()}")
print(f"Data da Competição: {competicao1.getDataCompeticao()}\n")

competicao2 = Competicao()
competicao2.setListaParticipantes(detetive1)
competicao2.setListaParticipantes(detetive2)
competicao2.setListaParticipantes(detetive3)
competicao2.setListaParticipantes(detetive4)
competicao2.setListaParticipantes(detetive5)
competicao2.setDataCompeticao("31/10/2017")
print("Competição 2")
print(f"Participantes: {competicao2.getListaParticipantes()[0].getNome()}, {competicao2.getListaParticipantes()[1].getNome()}, {competicao2.getListaParticipantes()[2].getNome()}, {competicao2.getListaParticipantes()[3].getNome()}, {competicao2.getListaParticipantes()[4].getNome()}")
print(f"Data da Competição: {competicao2.getDataCompeticao()}\n")

competicao3 = Competicao()
competicao3.setListaParticipantes(detetive1)
competicao3.setListaParticipantes(detetive2)
competicao3.setListaParticipantes(detetive3)
competicao3.setListaParticipantes(detetive4)
competicao3.setListaParticipantes(detetive5)
competicao3.setListaParticipantes(detetive6)
competicao3.setDataCompeticao("31/10/2018 - Edição Atual")
print("Competição 3")
print(f"Participantes: {competicao3.getListaParticipantes()[0].getNome()}, {competicao3.getListaParticipantes()[1].getNome()}, {competicao3.getListaParticipantes()[2].getNome()}, {competicao3.getListaParticipantes()[3].getNome()}, {competicao3.getListaParticipantes()[4].getNome()}, {competicao3.getListaParticipantes()[5].getNome()}")
print(f"Data da Competição: {competicao3.getDataCompeticao()}\n")

ranking1 = Ranking()
ranking1.setListaDetetives(detetive1)
ranking1.setListaDetetives(detetive3)
ranking1.setListaDetetives(detetive5)
ranking1.setPontuacoes(741)
ranking1.setPontuacoes(568)
ranking1.setPontuacoes(243)
print("Ranking 1")
print(f"Detetives e Pontuações: \n{ranking1.getListaDetetives()[0].getNome()} - {ranking1.getPontuacoes()[0]}\n{ranking1.getListaDetetives()[1].getNome()} - {ranking1.getPontuacoes()[1]}\n{ranking1.getListaDetetives()[2].getNome()} - {ranking1.getPontuacoes()[2]}\n")

ranking2 = Ranking()
ranking2.setListaDetetives(detetive6)
ranking2.setListaDetetives(detetive2)
ranking2.setListaDetetives(detetive4)
ranking2.setPontuacoes(1250)
ranking2.setPontuacoes(895)
ranking2.setPontuacoes(546)
print("Ranking 2")
print(f"Detetives e Pontuações: \n{ranking2.getListaDetetives()[0].getNome()} - {ranking2.getPontuacoes()[0]}\n{ranking2.getListaDetetives()[1].getNome()} - {ranking2.getPontuacoes()[1]}\n{ranking2.getListaDetetives()[2].getNome()} - {ranking2.getPontuacoes()[2]}\n")

ranking3 = Ranking()
ranking3.setListaDetetives(detetive4)
ranking3.setListaDetetives(detetive2)
ranking3.setListaDetetives(detetive3)
ranking3.setPontuacoes(890)
ranking3.setPontuacoes(315)
ranking3.setPontuacoes(178)
print("Ranking 3")
print(f"Detetives e Pontuações: \n{ranking3.getListaDetetives()[0].getNome()} - {ranking3.getPontuacoes()[0]}\n{ranking3.getListaDetetives()[1].getNome()} - {ranking3.getPontuacoes()[1]}\n{ranking3.getListaDetetives()[2].getNome()} - {ranking3.getPontuacoes()[2]}\n")

trofeu1 = Trofeu()
trofeu1.setDetetiveVencedor(detetive1)
trofeu1.setAnoVitoria(competicao1)
trofeu1.setFraseVitoria("O detetive Peralta é um sensacional detetine/gênio!")
print("Vencedor 1")
print(f"Detetive Vencedor: {trofeu1.getDetetiveVencedor().getNome()}")
print(f"Ano da Vitória: {trofeu1.getAnoVitoria().getDataCompeticao()}")
print(f"Frase da Vitória: {trofeu1.getFraseVitoria()}\n")

trofeu2 = Trofeu()
trofeu2.setDetetiveVencedor(detetive6)
trofeu2.setAnoVitoria(competicao2)
trofeu2.setFraseVitoria("O capitão de polícia Holt é um ótimo detetine/gênio!")
print("Vencedor 2")
print(f"Detetive Vencedor: {trofeu2.getDetetiveVencedor().getNome()}")
print(f"Ano da Vitória: {trofeu2.getAnoVitoria().getDataCompeticao()}")
print(f"Frase da Vitória: {trofeu2.getFraseVitoria()}\n")

trofeu3 = Trofeu()
trofeu3.setDetetiveVencedor(detetive2)
trofeu3.setAnoVitoria(competicao3)
trofeu3.setFraseVitoria("Amy Santiago é uma detetive incrível/gênio!")
print("Vencedor 3")
print(f"Detetive Vencedor: {trofeu3.getDetetiveVencedor().getNome()}")
print(f"Ano da Vitória: {trofeu3.getAnoVitoria().getDataCompeticao()}")
print(f"Frase da Vitória: {trofeu3.getFraseVitoria()}\n")