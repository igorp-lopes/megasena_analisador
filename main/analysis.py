import pandas as pd
import webscrap
from time import sleep
from utilities import displayHeader, testValidInput
from datetime import datetime
from dateutil.relativedelta import relativedelta


def selectDateInterval(dataframe, timeAgo, option):

    endInter = datetime.now()  # Salvamos a data atual como o final do intervalo

    if option == 'Anos':  # Se a opção escolhida é de trabalhar com o tempo em anos
        timeAgo *= 12  # Transformamos a escala de tempo de anos para meses

    # Subtraimos da data atual o tempo desejado
    startInter = endInter - relativedelta(months=timeAgo)

    # Guardamos apenas a parte da data dos dados do tipo datetime
    endInter = endInter.date()
    startInter = startInter.date()

    # Criamos uma máscara de seleção considerando o intervalo de tempo desejado
    selectionMask = (dataframe['Data Sorteio'] > startInter) & (
        dataframe["Data Sorteio"] <= endInter)

    # Retornamos o dataframe com a máscara de seleção aplicada
    return dataframe.loc[selectionMask]


def findRecurrency(option, dataframe):

    # Selecionamos apenas as colunas que indicam os números sorteados
    dfNums = dataframe.iloc[:, 2:8]

    # Series que armazenará o total de ocorrências de cada número
    ocurr = pd.Series([])

    for (column, data) in dfNums.iteritems():  # Iteramos pelo data frame coluna a coluna
        # Contamos as ocorrências de cada número na coluna
        temp = (data.value_counts()).sort_index()
        # Somamos as ocorrências da coluna com as ocorrências das colunas anteriores
        ocurr = ocurr.add(temp, fill_value=0)

    tot = int(ocurr.sum())  # Soma de todas as ocorrências de cada número

    # Dataframe que guardará as informações de ocorrência de cada número
    dfOcorr = pd.DataFrame([])

    # Criamos a coluna das ocorrências
    dfOcorr['Número de Ocorrências'] = ocurr

    # Lambda usado para calcular a porcentagem
    def percentage(x): return (x/tot) * 100
    # Criamos a coluna das porcentagens
    dfOcorr['% Total'] = ocurr.apply(percentage)
    index = dfOcorr.index  # Obtemos os indíces do dataframe

    if option == 'Specific Number':

        while(True):
            displayHeader()
            print("Qual o número para pesquisar sua ocorrência?\n")
            # Testamos se a entrada é um dos números presentes na cartela da megasena
            numEsc = testValidInput(1, 60)

            if numEsc:  # Se o valor recebido é um número válido

                # Selecionamos o número desejado no dataframe considerando a indexação começando no 0
                df_temp = dfOcorr.loc[index == numEsc]

                # Se o dataframe está vazio
                if df_temp.empty:
                    print(f"\nO número {numEsc} não foi sorteado nenhuma vez")
                else:

                    # Obtemos o total de ocorrências do número desejado
                    ocorr = df_temp.iloc[0, 0]
                    print(f"\nO número {numEsc} foi sorteado {ocorr} vezes")
                print("Pressione enter para continuar\n")
                input()
                break

    else:
        displayHeader()  # Mostramos o cabeçalho
        if option == 'mais frequentes':
            # Ordenamos o dataframe em ordem decrescente
            dfOcorr.sort_values('% Total', inplace=True, ascending=False)

        elif option == 'menos frequentes':
            # Ordenamos o dataframe em ordem crescente
            dfOcorr.sort_values('% Total', inplace=True, ascending=True)

        # Exibimos os 6 números mais/menos recorrentes
        print(f"Os números {option} são:")
        for num, ocorr in (dfOcorr.iloc[:6, 0]).items():
            print(f"{num} - foi sorteado {int(ocorr)} vezes\n")

        print("Pressione enter para continuar\n")
        input()

    return
