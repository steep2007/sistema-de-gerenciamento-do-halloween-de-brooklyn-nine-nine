from classes.detetive import Detetive
from classes.alianca import Alianca
from classes.peca import Peca
from classes.estrategia import Estrategia
from classes.competicao import Competicao
from classes.regras import Regras
from classes.ranking import Ranking
from classes.trofeu import Trofeu

import mysql.connector
class Arquivo:
    def lerDetetive1(self):
        with open('arquivos txt/detetiveN.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive2(self):
        with open('arquivos txt/detetiveS.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive3(self):
        with open('arquivos txt/detetiveC.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive4(self):
        with open('arquivos txt/detetiveP.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive5(self):
        with open('arquivos txt/detetive2_cargo.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive6(self):
        with open('arquivos txt/detetive2_nome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive7(self):
        with open('arquivos txt/detetive2_participacao_anterior.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive8(self):
        with open('arquivos txt/detetive2_sobrenome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive9(self):
        with open('arquivos txt/detetive3_nome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive10(self):
        with open('arquivos txt/detetive3_sobrenome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive11(self):
        with open('arquivos txt/detetive3_cargo.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive12(self):
        with open('arquivos txt/detetive3_participacao_anterior.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive13(self):
        with open('arquivos txt/detetive4_nome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive14(self):
        with open('arquivos txt/detetive4_sobrenome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive15(self):
        with open('arquivos txt/detetive4_cargo.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive16(self):
        with open('arquivos txt/detetive4_participacao_anterior.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive17(self):
        with open('arquivos txt/detetive5_nome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive18(self):
        with open('arquivos txt/detetive5_sobrenome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive19(self):
        with open('arquivos txt/detetive5_cargo.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive20(self):
        with open('arquivos txt/detetive5_participacao_anterior.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive21(self):
        with open('arquivos txt/detetive6_nome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive22(self):
        with open('arquivos txt/detetive6_sobrenome.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive23(self):
        with open('arquivos txt/detetive6_cargo.txt', "r") as detetive:
            return detetive.read()

    def lerDetetive24(self):
        with open('arquivos txt/detetive6_participacao_anterior.txt', "r") as detetive:
            return detetive.read()

    def lerAlianca1(self):
        with open('arquivos txt/alianca1.txt', "r") as alianca:
            return alianca.read()

    def lerAlianca2(self):
        with open('arquivos txt/alianca2.txt', "r") as alianca:
            return alianca.read()

    def lerAlianca3(self):
        with open('arquivos txt/alianca3.txt', "r") as alianca:
            return alianca.read()

    def lerCompeticao1(self):
        with open('arquivos txt/competicao1_lista_participantes.txt', "r") as competicao:
            return competicao.read()

    def lerCompeticao2(self):
        with open('arquivos txt/competicao1_data_competicao.txt', "r") as competicao:
            return competicao.read()

    def lerCompeticao3(self):
        with open('arquivos txt/competicao2_lista_participantes.txt', "r") as competicao:
            return competicao.read()

    def lerCompeticao4(self):
        with open('arquivos txt/competicao2_data_competicao.txt', "r") as competicao:
            return competicao.read()

    def lerCompeticao5(self):
        with open('arquivos txt/competicao3_lista_participantes.txt', "r") as competicao:
            return competicao.read()

    def lerCompeticao6(self):
        with open('arquivos txt/competicao3_data_competicao.txt', "r") as competicao:
            return competicao.read()

    def lerEstrategia1(self):
        with open('arquivos txt/estrategia1_detetive.txt', "r") as estrategia:
            return estrategia.read()
    def lerEstrategia2(self):
        with open('arquivos txt/estrategia1_lista_acoes.txt', "r") as estrategia:
            return estrategia.read()

    def lerEstrategia3(self):
        with open('arquivos txt/estrategia2_detetive.txt', "r") as estrategia:
            return estrategia.read()
    def lerEstrategia4(self):
        with open('arquivos txt/estrategia2_lista_acoes.txt', "r") as estrategia:
            return estrategia.read()

    def lerEstrategia5(self):
        with open('arquivos txt/estrategia3_detetive.txt', "r") as estrategia:
            return estrategia.read()

    def lerEstrategia6(self):
        with open('arquivos txt/estrategia3_lista_acoes.txt', "r") as estrategia:
            return estrategia.read()

    def lerEstrategia7(self):
        with open('arquivos txt/estrategia4_detetive.txt', "r") as estrategia:
            return estrategia.read()

    def lerEstrategia8(self):
        with open('arquivos txt/estrategia4_lista_acoes.txt', "r") as estrategia:
            return estrategia.read()
    def lerPeca1(self):
        with open('arquivos txt/peca1_detetive.txt', "r") as peca:
            return peca.read()

    def lerPeca2(self):
        with open('arquivos txt/peca1_descricao.txt', "r") as peca:
            return peca.read()

    def lerPeca3(self):
        with open('arquivos txt/peca2_detetive.txt', "r") as peca:
            return peca.read()

    def lerPeca4(self):
        with open('arquivos txt/peca2_descricao.txt', "r") as peca:
            return peca.read()

    def lerPeca5(self):
        with open('arquivos txt/peca3_detetive.txt', "r") as peca:
            return peca.read()

    def lerPeca6(self):
        with open('arquivos txt/peca3_descricao.txt', "r") as peca:
            return peca.read()

    def lerPeca7(self):
        with open('arquivos txt/peca4_detetive.txt', "r") as peca:
            return peca.read()

    def lerPeca8(self):
        with open('arquivos txt/peca4_descricao.txt', "r") as peca:
            return peca.read()

    def lerRegras1(self):
        with open('arquivos txt/regras1_restricoes.txt', "r") as regras:
            return regras.read()
    def lerRegras2(self):
        with open('arquivos txt/regras1_duracao.txt', "r") as regras:
            return regras.read()

    def lerRegras3(self):
        with open('arquivos txt/regras2_restricoes.txt', "r") as regras:
            return regras.read()
    def lerRegras4(self):
        with open('arquivos txt/regras2_duracao.txt', "r") as regras:
            return regras.read()

    def lerRegras5(self):
        with open('arquivos txt/regras3_restricoes.txt', "r") as regras:
            return regras.read()
    def lerRegras6(self):
        with open('arquivos txt/regras3_duracao.txt', "r") as regras:
            return regras.read()

    def lerRanking1(self):
        with open('arquivos txt/ranking1_detetives.txt', "r") as ranking:
            return ranking.read()

    def lerRanking2(self):
        with open('arquivos txt/ranking1_pontos.txt', "r") as ranking:
            return ranking.read()

    def lerRanking3(self):
        with open('arquivos txt/ranking2_detetives.txt', "r") as ranking:
            return ranking.read()

    def lerRanking4(self):
        with open('arquivos txt/ranking2_pontos.txt', "r") as ranking:
            return ranking.read()

    def lerRanking5(self):
        with open('arquivos txt/ranking3_detetives.txt', "r") as ranking:
            return ranking.read()

    def lerRanking6(self):
        with open('arquivos txt/ranking3_pontos.txt', "r") as ranking:
            return ranking.read()

    def lerTrofeu1(self):
        with open('arquivos txt/trofeu1_detetive_vencedor.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu2(self):
        with open('arquivos txt/trofeu1_ano_vitoria.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu3(self):
        with open('arquivos txt/trofeu1_frase_vitoria.txt', "r") as trofeu:
            return trofeu.read()

    def lerTrofeu4(self):
        with open('arquivos txt/trofeu2_detetive_vencedor.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu5(self):
        with open('arquivos txt/trofeu2_ano_vitoria.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu6(self):
        with open('arquivos txt/trofeu2_frase_vitoria.txt', "r") as trofeu:
            return trofeu.read()

    def lerTrofeu7(self):
        with open('arquivos txt/trofeu3_detetive_vencedor.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu8(self):
        with open('arquivos txt/trofeu3_ano_vitoria.txt', "r") as trofeu:
            return trofeu.read()
    def lerTrofeu9(self):
        with open('arquivos txt/trofeu3_frase_vitoria.txt', "r") as trofeu:
            return trofeu.read()

    def escreverDetetiveN(self):
        with open("arquivos txt/detetiveN.txt", "w") as detetive:
            detetive.write(detetive1.getNome() + ' ')

    def escreverDetetiveS(self):
        with open("arquivos txt/detetiveS.txt", "w") as detetive:
            detetive.write(detetive1.getSobrenome() + ' ')

    def escreverDetetiveC(self):
        with open("arquivos txt/detetiveC.txt", "w") as detetive:
            detetive.write(detetive1.getCargo() + ' ')
    def escreverDetetiveP(self):
        with open("arquivos txt/detetiveP.txt", "w") as detetive:
            detetive.write(detetive1.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive2(self):
        with open("arquivos txt/detetive2_nome.txt", "w") as detetive:
            detetive.write(detetive2.getNome() + ' ')

    def escreverSobrenomeDetetive2(self):
        with open("arquivos txt/detetive2_sobrenome.txt", "w") as detetive:
            detetive.write(detetive2.getSobrenome() + ' ')

    def escreverCargoDetetive2(self):
        with open("arquivos txt/detetive2_cargo.txt", "w") as detetive:
            detetive.write(detetive2.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive2(self):
        with open("arquivos txt/detetive2_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive2.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive3(self):
        with open("arquivos txt/detetive3_nome.txt", "w") as detetive:
            detetive.write(detetive3.getNome() + ' ')

    def escreverSobrenomeDetetive3(self):
        with open("arquivos txt/detetive3_sobrenome.txt", "w") as detetive:
            detetive.write(detetive3.getSobrenome() + ' ')

    def escreverCargoDetetive3(self):
        with open("arquivos txt/detetive3_cargo.txt", "w") as detetive:
            detetive.write(detetive3.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive3(self):
        with open("arquivos txt/detetive3_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive3.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive4(self):
        with open("arquivos txt/detetive4_nome.txt", "w") as detetive:
            detetive.write(detetive4.getNome() + ' ')

    def escreverSobrenomeDetetive4(self):
        with open("arquivos txt/detetive4_sobrenome.txt", "w") as detetive:
            detetive.write(detetive4.getSobrenome() + ' ')

    def escreverCargoDetetive4(self):
        with open("arquivos txt/detetive4_cargo.txt", "w") as detetive:
            detetive.write(detetive4.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive4(self):
        with open("arquivos txt/detetive4_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive4.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive5(self):
        with open("arquivos txt/detetive5_nome.txt", "w") as detetive:
            detetive.write(detetive5.getNome() + ' ')

    def escreverSobrenomeDetetive5(self):
        with open("arquivos txt/detetive5_sobrenome.txt", "w") as detetive:
            detetive.write(detetive5.getSobrenome() + ' ')

    def escreverCargoDetetive5(self):
        with open("arquivos txt/detetive5_cargo.txt", "w") as detetive:
            detetive.write(detetive5.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive5(self):
        with open("arquivos txt/detetive5_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive5.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive6(self):
        with open("arquivos txt/detetive6_nome.txt", "w") as detetive:
            detetive.write(detetive6.getNome() + ' ')

    def escreverSobrenomeDetetive6(self):
        with open("arquivos txt/detetive6_sobrenome.txt", "w") as detetive:
            detetive.write(detetive6.getSobrenome() + ' ')

    def escreverCargoDetetive6(self):
        with open("arquivos txt/detetive6_cargo.txt", "w") as detetive:
            detetive.write(detetive6.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive6(self):
        with open("arquivos txt/detetive6_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive6.getParticipacaoAnterior() + ' ')

    def escreverNomeDetetive7(self):
        with open("arquivos txt/detetive7_nome.txt", "w") as detetive:
            detetive.write(detetive7.getNome() + ' ')

    def escreverSobrenomeDetetive7(self):
        with open("arquivos txt/detetive7_sobrenome.txt", "w") as detetive:
            detetive.write(detetive7.getSobrenome() + ' ')

    def escreverCargoDetetive7(self):
        with open("arquivos txt/detetive7_cargo.txt", "w") as detetive:
            detetive.write(detetive7.getCargo() + ' ')

    def escreverParticipacaoAnteriorDetetive7(self):
        with open("arquivos txt/detetive7_participacao_anterior.txt", "w") as detetive:
            detetive.write(detetive7.getParticipacaoAnterior() + ' ')
    def escreverAlianca1(self):
        with open("arquivos txt/alianca1.txt", "w") as alianca:
            alianca.write(alianca1.getDetetivesAliados()[0].getNome() + ' e ' + alianca1.getDetetivesAliados()[1].getNome())

    def escreverAlianca2(self):
        with open("arquivos txt/alianca2.txt", "w") as alianca:
            alianca.write(alianca2.getDetetivesAliados()[0].getNome() + ' e ' + alianca2.getDetetivesAliados()[1].getNome())

    def escreverAlianca3(self):
        with open("arquivos txt/alianca3.txt", "w") as alianca:
            alianca.write(alianca3.getDetetivesAliados()[0].getNome() + ' e ' + alianca3.getDetetivesAliados()[1].getNome())

    def escreverPecaDetetive1(self):
        with open('arquivos txt/peca1_detetive.txt', "w") as peca:
            peca.write(peca1.getDetetiveResponsavel().getNome())

    def escreverPecaDescricao1(self):
        with open('arquivos txt/peca1_descricao.txt', "w") as peca:
            peca.write(peca1.getDescricaoPeca())

    def escreverPecaDetetive2(self):
        with open('arquivos txt/peca2_detetive.txt', "w") as peca:
            peca.write(peca2.getDetetiveResponsavel().getNome())

    def escreverPecaDescricao2(self):
        with open('arquivos txt/peca2_descricao.txt', "w") as peca:
            peca.write(peca2.getDescricaoPeca())
    def escreverPecaDetetive3(self):
        with open('arquivos txt/peca3_detetive.txt', "w") as peca:
            peca.write(peca3.getDetetiveResponsavel().getNome())

    def escreverPecaDescricao3(self):
        with open('arquivos txt/peca3_descricao.txt', "w") as peca:
            peca.write(peca3.getDescricaoPeca())

    def escreverPecaDetetive4(self):
        with open('arquivos txt/peca4_detetive.txt', "w") as peca:
            peca.write(peca4.getDetetiveResponsavel().getNome())

    def escreverPecaDescricao4(self):
        with open('arquivos txt/peca4_descricao.txt', "w") as peca:
            peca.write(peca4.getDescricaoPeca())

    def escreverEstrategiaDetetive1(self):
        with open('arquivos txt/estrategia1_detetive.txt', "w") as estrategia:
            estrategia.write(estrategia1.getDetetive().getNome())

    def escreverEstrategiaListaAcoes1(self):
        with open('arquivos txt/estrategia1_lista_acoes.txt', "w") as estrategia:
            estrategia.write(estrategia1.getListaAcoes())

    def escreverEstrategiaDetetive2(self):
        with open('arquivos txt/estrategia2_detetive.txt', "w") as estrategia:
            estrategia.write(estrategia2.getDetetive().getNome())

    def escreverEstrategiaListaAcoes2(self):
        with open('arquivos txt/estrategia2_lista_acoes.txt', "w") as estrategia:
            estrategia.write(estrategia2.getListaAcoes())

    def escreverEstrategiaDetetive3(self):
        with open('arquivos txt/estrategia3_detetive.txt', "w") as estrategia:
            estrategia.write(estrategia3.getDetetive().getNome())

    def escreverEstrategiaListaAcoes3(self):
        with open('arquivos txt/estrategia3_lista_acoes.txt', "w") as estrategia:
            estrategia.write(estrategia3.getListaAcoes())

    def escreverEstrategiaDetetive4(self):
        with open('arquivos txt/estrategia4_detetive.txt', "w") as estrategia:
            estrategia.write(estrategia4.getDetetive().getNome())

    def escreverEstrategiaListaAcoes4(self):
        with open('arquivos txt/estrategia4_lista_acoes.txt', "w") as estrategia:
            estrategia.write(estrategia4.getListaAcoes())

    def escreverCompeticaoParticipantes1(self):
        with open('arquivos txt/competicao1_lista_participantes.txt', "w") as competicao:
            competicao.write(competicao1.getListaParticipantes()[0].getNome() + ',' + competicao1.getListaParticipantes()[1].getNome() + ',' + competicao1.getListaParticipantes()[2].getNome() + ',' + competicao1.getListaParticipantes()[3].getNome())
    def escreverCompeticaoDataCompeticao1(self):
        with open('arquivos txt/competicao1_data_competicao.txt', "w") as competicao:
            competicao.write(competicao1.getDataCompeticao())

    def escreverCompeticaoParticipantes2(self):
        with open('arquivos txt/competicao2_lista_participantes.txt', "w") as competicao:
            competicao.write(competicao2.getListaParticipantes()[0].getNome() + ',' + competicao2.getListaParticipantes()[1].getNome() + ',' + competicao2.getListaParticipantes()[2].getNome() + ',' + competicao2.getListaParticipantes()[3].getNome() + ',' + competicao2.getListaParticipantes()[4].getNome() + ',' + competicao2.getListaParticipantes()[5].getNome())
    def escreverCompeticaoDataCompeticao2(self):
        with open('arquivos txt/competicao2_data_competicao.txt', "w") as competicao:
            competicao.write(competicao2.getDataCompeticao())

    def escreverCompeticaoParticipantes3(self):
        with open('arquivos txt/competicao3_lista_participantes.txt', "w") as competicao:
            competicao.write(competicao3.getListaParticipantes()[0].getNome() + ',' + competicao3.getListaParticipantes()[1].getNome() + ',' + competicao3.getListaParticipantes()[2].getNome() + ',' + competicao3.getListaParticipantes()[3].getNome() + ',' + competicao3.getListaParticipantes()[4].getNome() + ',' + competicao3.getListaParticipantes()[5].getNome())
    def escreverCompeticaoDataCompeticao3(self):
        with open('arquivos txt/competicao3_data_competicao.txt', "w") as competicao:
            competicao.write(competicao3.getDataCompeticao())

    def escreverRegrasRestricoes1(self):
        with open('arquivos txt/regras1_restricoes.txt', "w") as regras:
            regras.write(regras1.getRestricoesLocal())

    def escreverRegrasDuracao1(self):
        with open('arquivos txt/regras1_duracao.txt', "w") as regras:
            regras.write(regras1.getDuracao())

    def escreverRegrasRestricoes2(self):
        with open('arquivos txt/regras2_restricoes.txt', "w") as regras:
            regras.write(regras2.getRestricoesLocal())

    def escreverRegrasDuracao2(self):
        with open('arquivos txt/regras2_duracao.txt', "w") as regras:
            regras.write(regras2.getDuracao())

    def escreverRegrasRestricoes3(self):
        with open('arquivos txt/regras3_restricoes.txt', "w") as regras:
            regras.write(regras3.getRestricoesLocal())

    def escreverRegrasDuracao3(self):
        with open('arquivos txt/regras3_duracao.txt', "w") as regras:
            regras.write(regras3.getDuracao())

    def escreverDetetiveRanking1(self):
        with open('arquivos txt/ranking1_detetives.txt', "w") as ranking:
            ranking.write('1 - ' + ranking1.getListaDetetives()[0].getNome()  + ' 2 - ' + ranking1.getListaDetetives()[1].getNome() + ' 3 - ' + ranking1.getListaDetetives()[2].getNome())
    def escreverPontosRanking1(self):
        with open('arquivos txt/ranking1_pontos.txt', "w") as ranking:
           ranking.write('1 - ' + str(ranking1.getPontuacoes()[0]) + ' 2 - ' + str(ranking1.getPontuacoes()[1]) + ' 3 - ' + str(ranking1.getPontuacoes()[2]))

    def escreverDetetiveRanking2(self):
        with open('arquivos txt/ranking2_detetives.txt', "w") as ranking:
            ranking.write('1 - ' + ranking2.getListaDetetives()[0].getNome() + ' 2 - ' + ranking2.getListaDetetives()[1].getNome() + ' 3 - ' + ranking2.getListaDetetives()[2].getNome())

    def escreverPontosRanking2(self):
        with open('arquivos txt/ranking2_pontos.txt', "w") as ranking:
            ranking.write('1 - ' + str(ranking2.getPontuacoes()[0]) + ' 2 - ' + str(ranking2.getPontuacoes()[1]) + ' 3 - ' + str(ranking2.getPontuacoes()[2]))
    def escreverDetetiveRanking3(self):
        with open('arquivos txt/ranking3_detetives.txt', "w") as ranking:
            ranking.write('1 - ' + ranking3.getListaDetetives()[0].getNome() + ' 2 - ' + ranking3.getListaDetetives()[1].getNome() + ' 3 - ' + ranking3.getListaDetetives()[2].getNome())

    def escreverPontosRanking3(self):
        with open('arquivos txt/ranking3_pontos.txt', "w") as ranking:
            ranking.write( '1 - ' + str(ranking3.getPontuacoes()[0]) + ' 2 - ' + str(ranking3.getPontuacoes()[1]) + ' 3 - ' + str(ranking3.getPontuacoes()[2]))

    def escreverDetetiveVencedorTrofeu1(self):
        with open('arquivos txt/trofeu1_detetive_vencedor.txt', "w") as trofeu:
            trofeu.write(trofeu1.getDetetiveVencedor().getNome())
    def escreverAnoVitoriaTrofeu1(self):
        with open('arquivos txt/trofeu1_ano_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu1.getAnoVitoria().getDataCompeticao())

    def escreverFraseVitoriaTrofeu1(self):
        with open('arquivos txt/trofeu1_frase_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu1.getFraseVitoria())

    def escreverDetetiveVencedorTrofeu2(self):
        with open('arquivos txt/trofeu2_detetive_vencedor.txt', "w") as trofeu:
            trofeu.write(trofeu2.getDetetiveVencedor().getNome())
    def escreverAnoVitoriaTrofeu2(self):
        with open('arquivos txt/trofeu2_ano_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu2.getAnoVitoria().getDataCompeticao())

    def escreverFraseVitoriaTrofeu2(self):
        with open('arquivos txt/trofeu2_frase_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu2.getFraseVitoria())

    def escreverDetetiveVencedorTrofeu3(self):
        with open('arquivos txt/trofeu3_detetive_vencedor.txt', "w") as trofeu:
            trofeu.write(trofeu3.getDetetiveVencedor().getNome())
    def escreverAnoVitoriaTrofeu3(self):
        with open('arquivos txt/trofeu3_ano_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu3.getAnoVitoria().getDataCompeticao())

    def escreverFraseVitoriaTrofeu3(self):
        with open('arquivos txt/trofeu3_frase_vitoria.txt', "w") as trofeu:
            trofeu.write(trofeu3.getFraseVitoria())

    def escreverBanco(self, banco, ip, usuario, senha, table):
        conexao = mysql.connector.connect(host=ip, user=usuario, port="3306", password=senha, database=banco)  # Estabelece a conexão com o banco de dados

        textoDetetive = self.lerDetetive1()
        textoDetetive2 = self.lerDetetive2()
        textoDetetive3 = self.lerDetetive3()
        textoDetetive4 = self.lerDetetive4()

        textoDetetive5 = self.lerDetetive5()
        textoDetetive6 = self.lerDetetive6()
        textoDetetive7 = self.lerDetetive7()
        textoDetetive8 = self.lerDetetive8()

        textoDetetive9 = self.lerDetetive9()
        textoDetetive10 = self.lerDetetive10()
        textoDetetive11 = self.lerDetetive11()
        textoDetetive12 = self.lerDetetive12()

        textoDetetive13 = self.lerDetetive13()
        textoDetetive14 = self.lerDetetive14()
        textoDetetive15 = self.lerDetetive15()
        textoDetetive16 = self.lerDetetive16()

        textoDetetive17 = self.lerDetetive17()
        textoDetetive18 = self.lerDetetive18()
        textoDetetive19 = self.lerDetetive19()
        textoDetetive20 = self.lerDetetive20()

        textoDetetive21 = self.lerDetetive21()
        textoDetetive22 = self.lerDetetive22()
        textoDetetive23 = self.lerDetetive23()
        textoDetetive24 = self.lerDetetive24()

        textoAlianca1 = self.lerAlianca1()
        textoAlianca2 = self.lerAlianca2()
        textoAlianca3 = self.lerAlianca3()

        textoPeca1 = self.lerPeca1()
        textoPeca2 = self.lerPeca2()
        textoPeca3 = self.lerPeca3()
        textoPeca4 = self.lerPeca4()
        textoPeca5 = self.lerPeca5()
        textoPeca6 = self.lerPeca6()
        textoPeca7 = self.lerPeca7()
        textoPeca8 = self.lerPeca8()

        textoEstrategia1 = self.lerEstrategia1()
        textoEstrategia2 = self.lerEstrategia2()
        textoEstrategia3 = self.lerEstrategia3()
        textoEstrategia4 = self.lerEstrategia4()
        textoEstrategia5 = self.lerEstrategia5()
        textoEstrategia6 = self.lerEstrategia6()
        textoEstrategia7 = self.lerEstrategia7()
        textoEstrategia8 = self.lerEstrategia8()

        textoCompeticao1 = self.lerCompeticao1()
        textoCompeticao2 = self.lerCompeticao2()

        textoCompeticao3 = self.lerCompeticao3()
        textoCompeticao4 = self.lerCompeticao4()

        textoCompeticao5 = self.lerCompeticao5()
        textoCompeticao6 = self.lerCompeticao6()

        textoRegras1 = self.lerRegras1()
        textoRegras2 = self.lerRegras2()
        textoRegras3 = self.lerRegras3()
        textoRegras4 = self.lerRegras4()
        textoRegras5 = self.lerRegras5()
        textoRegras6 = self.lerRegras6()

        textoRanking1 = self.lerRanking1()
        textoRanking2 = self.lerRanking2()

        textoRanking3 = self.lerRanking3()
        textoRanking4 = self.lerRanking4()

        textoRanking5 = self.lerRanking5()
        textoRanking6 = self.lerRanking6()

        textoTrofeu1 = self.lerTrofeu1()
        textoTrofeu2 = self.lerTrofeu2()
        textoTrofeu3 = self.lerTrofeu3()

        textoTrofeu4 = self.lerTrofeu4()
        textoTrofeu5 = self.lerTrofeu5()
        textoTrofeu6 = self.lerTrofeu6()

        textoTrofeu7 = self.lerTrofeu7()
        textoTrofeu8 = self.lerTrofeu8()
        textoTrofeu9 = self.lerTrofeu9()


        comandos = conexao.cursor()
        # comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive}', '{textoDetetive2}', '{textoDetetive3}', '{textoDetetive4}')")
        # comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive6}', '{textoDetetive8}', '{textoDetetive5}', '{textoDetetive7}')")
        # comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive9}', '{textoDetetive10}', '{textoDetetive11}', '{textoDetetive12}')")
        # comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive13}', '{textoDetetive14}', '{textoDetetive15}', '{textoDetetive16}')")
        # comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive17}', '{textoDetetive18}', '{textoDetetive19}', '{textoDetetive20}')")
        comandos.execute(f"INSERT INTO {table} (nome, sobrenome, cargo, participacaoAnterior) VALUES ('{textoDetetive21}', '{textoDetetive22}', '{textoDetetive23}', '{textoDetetive24}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id) VALUES ('{textoAlianca1}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id) VALUES ('{textoAlianca2}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id) VALUES ('{textoAlianca3}')")
        # comandos.execute(f"INSERT INTO {table} (detetiveResponsavel, descricaoPeca) VALUES ('{textoPeca1}', '{textoPeca2}')")
        # comandos.execute(f"INSERT INTO {table} (detetiveResponsavel, descricaoPeca) VALUES ('{textoPeca3}', '{textoPeca4}')")
        # comandos.execute(f"INSERT INTO {table} (detetiveResponsavel, descricaoPeca) VALUES ('{textoPeca5}', '{textoPeca6}')")
        # comandos.execute(f"INSERT INTO {table} (detetiveResponsavel, descricaoPeca) VALUES ('{textoPeca7}', '{textoPeca8}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, listaAcoes) VALUES ('{textoEstrategia1}', '{textoEstrategia2}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, listaAcoes) VALUES ('{textoEstrategia3}', '{textoEstrategia4}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, listaAcoes) VALUES ('{textoEstrategia5}', '{textoEstrategia6}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, listaAcoes) VALUES ('{textoEstrategia7}', '{textoEstrategia8}')")

        # comandos.execute(f"INSERT INTO {table} (listaParticipantes, dataCompeticao) VALUES ('{textoCompeticao1}', '{textoCompeticao2}')")
        # comandos.execute(f"INSERT INTO {table} (listaParticipantes, dataCompeticao) VALUES ('{textoCompeticao3}', '{textoCompeticao4}')")
        # comandos.execute(f"INSERT INTO {table} (listaParticipantes, dataCompeticao) VALUES ('{textoCompeticao5}', '{textoCompeticao6}')")

        # comandos.execute(f"INSERT INTO {table} (restricoesLocal, duracao) VALUES ('{textoRegras1}', '{textoRegras2}')")
        # comandos.execute(f"INSERT INTO {table} (restricoesLocal, duracao) VALUES ('{textoRegras3}', '{textoRegras4}')")
        # comandos.execute(f"INSERT INTO {table} (restricoesLocal, duracao) VALUES ('{textoRegras5}', '{textoRegras6}')")
        # comandos.execute(f"INSERT INTO {table} (listaDetetives, pontuacoes) VALUES ('{textoRanking1}', '{textoRanking2}')")
        # comandos.execute(f"INSERT INTO {table} (listaDetetives, pontuacoes) VALUES ('{textoRanking3}', '{textoRanking4}')")
        # comandos.execute(f"INSERT INTO {table} (listaDetetives, pontuacoes) VALUES ('{textoRanking5}', '{textoRanking6}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, anoVitoria, fraseVitoria) VALUES ('{textoTrofeu1}', '{textoTrofeu2}', '{textoTrofeu3}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, anoVitoria, fraseVitoria) VALUES ('{textoTrofeu4}', '{textoTrofeu5}', '{textoTrofeu6}')")
        # comandos.execute(f"INSERT INTO {table} (detetive_id, anoVitoria, fraseVitoria) VALUES ('{textoTrofeu7}', '{textoTrofeu8}', '{textoTrofeu9}')")

        conexao.commit()
        conexao.close()

    def lerBanco(self, banco, ip, usuario, senha, table):
        conexao = mysql.connector.connect(host=ip, user=usuario, port="3306", password=senha, database=banco)

        comandos = conexao.cursor()
        #query = "SELECT * from detetive"
        #query = "SELECT * from alianca"
        #query = "SELECT * from trofeu"
        #query = "SELECT * from ranking"
        #query = "SELECT * from peca"
        #query = "SELECT * from estrategia"
        query = "SELECT * from competicao"
        #query = "SELECT * from regras"
        comandos.execute(query)

        for linha in comandos:
            print(linha)


detetive1 = Detetive()
detetive1.setNome("Jake")
detetive1.setSobrenome("Peralta")
detetive1.setCargo("Detetive de Homicídios")
detetive1.setParticipacaoAnterior("Perdedor")
print("Detetive 1")
print("Nome: {}".format(detetive1.getNome()))
print("Sobrenome: {}".format(detetive1.getSobrenome()))
print("Cargo: {}".format(detetive1.getCargo()))
print("Participação Anterior: {}\n".format(detetive1.getParticipacaoAnterior()))

detetive2 = Detetive()
detetive2.setNome("Amy")
detetive2.setSobrenome("Santiago")
detetive2.setCargo("Detetive de Homicídios")
detetive2.setParticipacaoAnterior("Perdedor")
print("Detetive 2")
print("Nome: {}".format(detetive2.getNome()))
print("Sobrenome: {}".format(detetive2.getSobrenome()))
print("Cargo: {}".format(detetive2.getCargo()))
print("Participação Anterior: {}\n".format(detetive2.getParticipacaoAnterior()))

detetive3 = Detetive()
detetive3.setNome("Rosa")
detetive3.setSobrenome("Diaz")
detetive3.setCargo("Detetive de Homicídios")
detetive3.setParticipacaoAnterior("Perdedor")
print("Detetive 3")
print("Nome: {}".format(detetive3.getNome()))
print("Sobrenome: {}".format(detetive3.getSobrenome()))
print("Cargo: {}".format(detetive3.getCargo()))
print("Participação Anterior: {}\n".format(detetive3.getParticipacaoAnterior()))

detetive4 = Detetive()
detetive4.setNome("Terry")
detetive4.setSobrenome("Jeffords")
detetive4.setCargo("Sargento de Polícia")
detetive4.setParticipacaoAnterior("Perdedor")
print("Detetive 4")
print("Nome: {}".format(detetive4.getNome()))
print("Sobrenome: {}".format(detetive4.getSobrenome()))
print("Cargo: {}".format(detetive4.getCargo()))
print("Participação Anterior: {}\n".format(detetive4.getParticipacaoAnterior()))

detetive5 = Detetive()
detetive5.setNome("Charles")
detetive5.setSobrenome("Boyle")
detetive5.setCargo("Detetive de Homicídios")
detetive5.setParticipacaoAnterior("Perdedor")
print("Detetive 5")
print("Nome: {}".format(detetive5.getNome()))
print("Sobrenome: {}".format(detetive5.getSobrenome()))
print("Cargo: {}".format(detetive5.getCargo()))
print("Participação Anterior: {}\n".format(detetive5.getParticipacaoAnterior()))

detetive6 = Detetive()
detetive6.setNome("André")
detetive6.setSobrenome("Bezerra")
detetive6.setCargo("Capitão de Polícia")
detetive6.setParticipacaoAnterior("Vencedor")
print("Detetive 6")
print("Nome: {}".format(detetive6.getNome()))
print("Sobrenome: {}".format(detetive6.getSobrenome()))
print("Cargo: {}".format(detetive6.getCargo()))
print("Participação Anterior: {} \n".format(detetive6.getParticipacaoAnterior()))

alianca1 = Alianca()
alianca1.setDetetivesAliados(detetive6)
alianca1.setDetetivesAliados(detetive2)
print("Aliança 1")
print(f"Detetives Aliados: {alianca1.getDetetivesAliados()[0].getNome()} e {alianca1.getDetetivesAliados()[1].getNome()}\n")

alianca2 = Alianca()
alianca2.setDetetivesAliados(detetive1)
alianca2.setDetetivesAliados(detetive5)
print("Aliança 2")
print(f"Detetives Aliados: {alianca2.getDetetivesAliados()[0].getNome()} e {alianca2.getDetetivesAliados()[1].getNome()}\n")

alianca3 = Alianca()
alianca3.setDetetivesAliados(detetive1)
alianca3.setDetetivesAliados(detetive4)
print("Aliança 3")
print(f"Detetives Aliados: {alianca3.getDetetivesAliados()[0].getNome()} e {alianca3.getDetetivesAliados()[1].getNome()}\n")

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
competicao2.setListaParticipantes(detetive6)
competicao2.setDataCompeticao("31/10/2017")
print("Competição 2")
print(f"Participantes: {competicao2.getListaParticipantes()[0].getNome()}, {competicao2.getListaParticipantes()[1].getNome()}, {competicao2.getListaParticipantes()[2].getNome()}, {competicao2.getListaParticipantes()[3].getNome()}, {competicao2.getListaParticipantes()[4].getNome()}, {competicao2.getListaParticipantes()[5].getNome()}")
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
ranking3.setListaDetetives(detetive2)
ranking3.setListaDetetives(detetive4)
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

arq = Arquivo()

arq.escreverDetetiveN()
arq.escreverDetetiveS()
arq.escreverDetetiveC()
arq.escreverDetetiveP()

arq.escreverNomeDetetive2()
arq.escreverSobrenomeDetetive2()
arq.escreverCargoDetetive2()
arq.escreverParticipacaoAnteriorDetetive2()

arq.escreverNomeDetetive3()
arq.escreverSobrenomeDetetive3()
arq.escreverCargoDetetive3()
arq.escreverParticipacaoAnteriorDetetive3()

arq.escreverNomeDetetive4()
arq.escreverSobrenomeDetetive4()
arq.escreverCargoDetetive4()
arq.escreverParticipacaoAnteriorDetetive4()

arq.escreverNomeDetetive5()
arq.escreverSobrenomeDetetive5()
arq.escreverCargoDetetive5()
arq.escreverParticipacaoAnteriorDetetive5()

arq.escreverNomeDetetive6()
arq.escreverSobrenomeDetetive6()
arq.escreverCargoDetetive6()
arq.escreverParticipacaoAnteriorDetetive6()

arq.escreverAlianca1()
arq.escreverAlianca2()
arq.escreverAlianca3()

arq.escreverPecaDetetive1()
arq.escreverPecaDescricao1()

arq.escreverPecaDetetive2()
arq.escreverPecaDescricao2()

arq.escreverPecaDetetive3()
arq.escreverPecaDescricao3()

arq.escreverPecaDetetive4()
arq.escreverPecaDescricao4()

arq.escreverEstrategiaDetetive1()
arq.escreverEstrategiaListaAcoes1()

arq.escreverEstrategiaDetetive2()
arq.escreverEstrategiaListaAcoes2()

arq.escreverEstrategiaDetetive3()
arq.escreverEstrategiaListaAcoes3()

arq.escreverEstrategiaDetetive4()
arq.escreverEstrategiaListaAcoes4()

arq.escreverCompeticaoParticipantes1()
arq.escreverCompeticaoDataCompeticao1()

arq.escreverCompeticaoParticipantes2()
arq.escreverCompeticaoDataCompeticao2()

arq.escreverCompeticaoParticipantes3()
arq.escreverCompeticaoDataCompeticao3()

arq.escreverRegrasRestricoes1()
arq.escreverRegrasDuracao1()

arq.escreverRegrasRestricoes2()
arq.escreverRegrasDuracao2()

arq.escreverRegrasRestricoes3()
arq.escreverRegrasDuracao3()

arq.escreverDetetiveRanking1()
arq.escreverPontosRanking1()

arq.escreverDetetiveRanking2()
arq.escreverPontosRanking2()

arq.escreverDetetiveRanking3()
arq.escreverPontosRanking3()

arq.escreverDetetiveVencedorTrofeu1()
arq.escreverAnoVitoriaTrofeu1()
arq.escreverFraseVitoriaTrofeu1()

arq.escreverDetetiveVencedorTrofeu2()
arq.escreverAnoVitoriaTrofeu2()
arq.escreverFraseVitoriaTrofeu2()

arq.escreverDetetiveVencedorTrofeu3()
arq.escreverAnoVitoriaTrofeu3()
arq.escreverFraseVitoriaTrofeu3()

arq.escreverBanco("Classes", "localhost", "root", "", "detetive")
#arq.escreverBanco("Classes", "localhost", "root", "", "alianca")
#arq.escreverBanco("Classes", "localhost", "root", "", "peca")
#arq.escreverBanco("Classes", "localhost", "root", "", "competicao")
#arq.escreverBanco("Classes", "localhost", "root", "", "estrategia")
#arq.escreverBanco("Classes", "localhost", "root", "", "regras")
#arq.escreverBanco("Classes", "localhost", "root", "", "ranking")
#arq.escreverBanco("Classes", "localhost", "root", "", "trofeu")

#arq.lerBanco("Classes", "localhost", "root", "", "detetive")
#arq.lerBanco("Classes", "localhost", "root", "", "alianca")
#arq.lerBanco("Classes", "localhost", "root", "", "peca")
#arq.lerBanco("Classes", "localhost", "root", "", "estrategia")
arq.lerBanco("Classes", "localhost", "root", "", "competicao")
#arq.lerBanco("Classes", "localhost", "root", "", "regras")
#arq.lerBanco("Classes", "localhost", "root", "", "ranking")
#arq.lerBanco("Classes", "localhost", "root", "", "trofeu")