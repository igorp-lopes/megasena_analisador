import pandas as pd
import webscrap
from time import sleep
from utilities import displayHeader, testValidInput
from datetime import datetime
from datetime import date
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
    dataframe = dataframe.iloc[:, 2:8]

    # Series que armazenará o total de ocorrências de cada número
    ocurr = pd.Series([])

    for (_, data) in dataframe.iteritems():  # Iteramos pelo data frame coluna a coluna
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

# Função que retorna a data da ocorrência mais antiga de um número
def findLastOcurr(numEsc, dataframe):

    dataAnt = date(9999,12,31) # Valor inicial padrão maior do que todas as datas do dataframe para a comparação

    for column in dataframe.drop(["Data Sorteio"], axis = 1).columns:  # Iteramos pelo data frame coluna a coluna
        dfTemp = dataframe[['Data Sorteio', column]] # Criamos um dataframe temporário com as datas e a dezena atual
        dfTemp = dfTemp[dfTemp[column] == numEsc] # Selecionamos as datas em que o número escolhido for sorteado na dezena atual

        if not dfTemp.empty: # Se o dataframe não está vazio
            if dfTemp.iat[0,0] < dataAnt: # Se a data mais antiga da dezena atual é menor do que a menor data identificada anteriormente
                dataAnt = dfTemp.iat[0,0] # Atualizamos a data mais antiga indentificada

    return dataAnt # Retornamos a data da ocorrência mais antiga do número escolhido

def dataAnalysis(option,dataframe):

    if option == 'Specific Number':

        while(True):
            displayHeader()
            print("Qual o número para relacionar suas ocorrências com datas?\n")
            # Testamos se a entrada é um dos números presentes na cartela da megasena
            numEsc = testValidInput(1, 60)

            if numEsc:  # Se o valor recebido é um número válido

                # Obtemos a data da ocorrência mais antiga do número selecionado
                oldDate = findLastOcurr(numEsc, dataframe)

                # Se o dataframe está vazio
                if oldDate == None:
                    print(f"\nO número {numEsc} não foi sorteado nenhuma vez no período de tempo selecionado")

                else:
                    oldDate = oldDate.strftime("%d/%m/%Y") # Convertemos a data para o formato string
                    print(f"\nA data mais antiga em que o número {numEsc} foi sorteado é {oldDate}")

                print("Pressione enter para continuar\n")
                input()
                break
    
    else:
        pass
