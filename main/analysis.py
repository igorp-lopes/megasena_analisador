import pandas as pd
import webscrap
from time import sleep
from utilities import displayHeader, testValidInput
from datetime import datetime
from dateutil.relativedelta import relativedelta

def selectDateInterval(dataframe, timeAgo, option):

    endInter = datetime.now() # Salvamos a data atual como o final do intervalo

    if option == 'Anos': # Se a opção escolhida é de trabalhar com o tempo em anos
        timeAgo *= 12 # Transformamos a escala de tempo de anos para meses

    startInter = endInter - relativedelta(months = timeAgo) # Subtraimos da data atual o tempo desejado

    # Guardamos apenas a parte da data dos dados do tipo datetime
    endInter = endInter.date()
    startInter = startInter.date() 

    # Criamos uma máscara de seleção considerando o intervalo de tempo desejado
    selectionMask = (dataframe['Data Sorteio'] > startInter) & (dataframe["Data Sorteio"] <= endInter)

    return dataframe.loc[selectionMask] # Retornamos o dataframe com a máscara de seleção aplicada

def findRecurrency(option, dataframe):

    dfNums = dataframe.iloc[:,2:8] # Selecionamos apenas as colunas que indicam os números sorteados

    ocurr = pd.Series([]) # Series que armazenará o total de ocorrências de cada número

    for (column, data) in dfNums.iteritems(): # Iteramos pelo data frame coluna a coluna
        temp = ( data.value_counts() ).sort_index() # Contamos as ocorrências de cada número na coluna
        ocurr = ocurr.add(temp,fill_value=0) # Somamos as ocorrências da coluna com as ocorrências das colunas anteriores

    tot = int(ocurr.sum()) # Soma de todas as ocorrências de cada número

    dfOcorr = pd.DataFrame([]) # Dataframe que guardará as informações de ocorrência de cada número

    dfOcorr['Número de Ocorrências'] = ocurr # Criamos a coluna das ocorrências

    percentage = lambda x: (x/tot) * 100 # Lambda usado para calcular a porcentagem
    dfOcorr['% Total'] = ocurr.apply(percentage) # Criamos a coluna das porcentagens

    if option == 'Specific Number':

        while(True):
            displayHeader()
            print("Qual o número para pesquisar sua ocorrência?\n")
            numEsc = testValidInput(1,60) # Testamos se a entrada é um dos números presentes na cartela da megasena

            if numEsc: # Se o valor recebido é um número válido
                df_temp = dfOcorr.iloc[(numEsc-1), 0] # Selecionamos o número desejado no dataframe considerando a indexação começando no 0

                print(f"O número {numEsc} foi sorteado {df_temp} vezes")
                print("Pressione enter para continuar\n")
                input()
                break 

    else:
        displayHeader() # Mostramos o cabeçalho
        if option == 'mais frequentes':
            dfOcorr.sort_values('% Total', inplace = True, ascending = False) # Ordenamos o dataframe em ordem decrescente

        elif option == 'menos frequentes':
            dfOcorr.sort_values('% Total', inplace = True, ascending = True) # Ordenamos o dataframe em ordem crescente

        # Exibimos os 6 números mais/menos recorrentes
        print(f"Os números {option} são:")
        for num, ocorr in (dfOcorr.iloc[:6,0]).items():
            print(f"{num} - foi sorteado {int(ocorr)} vezes\n")

        print("Pressione enter para continuar\n")
        input()    

    return

        

