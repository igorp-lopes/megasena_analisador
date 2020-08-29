import pandas as pd
import webscrap
from time import sleep
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import itertools
from utilities import displayHeader, testValidInput

def selectDateInterval(dataframe, timeAgo):

    endInter = datetime.now()  # Salvamos a data atual como o final do intervalo

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
    dataframe = dataframe.iloc[:, 2:]

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
                    print(f"\nO número {numEsc} foi sorteado {int(ocorr)} vezes")
                print("\nPressione enter para continuar\n")
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
        print(f"Os números {option} são:\n")
        for num, ocorr in (dfOcorr.iloc[:, 0]).items():
            print(f"{num} - sorteado {int(ocorr)} vezes\n")

        print("Pressione enter para continuar\n")
        input()

    return

# Função que retorna as informações sobre as datas de ocorrências de um número

def findDateOcurr(numEsc, dataframe):

    dataNov = date(1990,12,31) # Valor inicial padrão da data mais recente menor do que todas as datas do dataframe para a comparação
    dataAnt = date(9999,12,31) # Valor inicial padrão da data mais antiga maior do que todas as datas do dataframe para a comparação

    for column in dataframe.drop(["Data Sorteio"], axis = 1).columns:  # Eliminamos a coluna das datas e iteramos pelo data frame coluna a coluna
        dfTemp = dataframe[['Data Sorteio', column]] # Criamos um dataframe temporário com as datas e a dezena atual
        dfTemp = dfTemp[dfTemp[column] == numEsc] # Selecionamos as datas em que o número escolhido for sorteado na dezena atual

        if not dfTemp.empty: # Se o dataframe não está vazio

            dataIndex = dfTemp.index[-1] # Obtemos índice da data mais recente no dataframe atual

            if dfTemp['Data Sorteio'].loc[dataIndex] > dataNov: # Se a data mais recente da dezena atual é mais recente do que a mais recente data identificada anteriormente
                dataNov = dfTemp['Data Sorteio'].loc[dataIndex] # Atualizamos a data mais antiga indentificada

            dataIndex = dfTemp.index[0] # Obtemos índice da data mais antiga no dataframe atual

            if dfTemp['Data Sorteio'].loc[dataIndex] < dataAnt: # Se a data mais antiga da dezena atual é mais antiga do que a mais antiga data identificada anteriormente
                dataAnt = dfTemp['Data Sorteio'].loc[dataIndex] # Atualizamos a data mais antiga indentificada

    if dataNov == date(1990,12,31): # Se não há alteração no valor inicial padrão, ou seja, não há ocorrências do número
        return None, None

    return dataNov, dataAnt


def dateAnalysis(option,dataframe):

    class ocurrDates():

        def __init__(self, number, newDate, oldDate):
            self.number = number
            self.newestDate = newDate
            self.oldestDate = oldDate

        def returnDates(self):
            return self.newestDate, self.oldestDate

    # Selecionamos apenas as colunas que indicam a data dos sorteios e os números sorteados
    dataframe = dataframe.iloc[:, 1:8]

    if option == 'Specific Number':

        while(True):
            displayHeader()
            print("Qual o número para relacionar suas ocorrências com datas?\n")
            # Testamos se a entrada é um dos números presentes na cartela da megasena
            numEsc = testValidInput(1, 60)

            if numEsc:  # Se o valor recebido é um número válido

                # Obtemos a data da ocorrência mais antiga do número selecionado
                newDate, oldDate = findDateOcurr(numEsc, dataframe)

                # Se o dataframe está vazio
                if oldDate == None:
                    print(f"\nO número {numEsc} não foi sorteado nenhuma vez no período de tempo selecionado")

                else:
                    oldDate = oldDate.strftime("%d/%m/%Y") # Convertemos a data para o formato string
                    print(f"\nA primeira vez em que o número {numEsc} foi sorteado foi em {oldDate}")
                    newDate = newDate.strftime("%d/%m/%Y") # Convertemos a data para o formato string
                    print(f"\nA última vez em que o número {numEsc} foi sorteado foi em {newDate}")

                break
    
    else:
        
        listDate = [] # Lista que armazena as datas das ocorrências
        # Para cada um dos possíveis números
        for number in itertools.count(1):
            
            # Condição de saída do loop
            if number > 60:
                break

            # Obtemos as datas das ocorrências mais recente e mais nova do número atual
            dataNov, dataAnt = findDateOcurr(number, dataframe)

            # Se houve ocorrência do número
            if dataNov != None:
                numDates = ocurrDates(number, dataNov, dataAnt) # Instanciamos um objeto para guardar as datas
                listDate.append(numDates) # Salvamos o objeto na lista

        displayHeader()

        if(option == "Most Recent"):
            listDate.sort(key = lambda x: x.newestDate, reverse = False) # Ordenamos a lista pela data mais recente
            print("\nOrdenando os números pela última vez em que eles foram sorteados\n")

            for date in listDate:

                if date.newestDate == None:
                    print(f"{date.number} não foi sorteado nenhuma vez")

                else:
                    newDate = date.newestDate.strftime("%d/%m/%Y") # Convertemos a data para o formato string
                    print(f"{date.number} - {newDate}")


        else:
            listDate.sort(key = lambda x: x.oldestDate, reverse = False) # Ordenamos a lista pela data mais antiga
            print("\nOrdenando os números pela primeira vez em que eles foram sorteados\n")
            
            for date in listDate:

                if date.oldestDate == None:
                    print(f"{date.number} não foi sorteado nenhuma vez")

                else:
                    oldDate = date.oldestDate.strftime("%d/%m/%Y") # Convertemos a data para o formato string
                    print(f"{date.number} - {oldDate}")

    print("\nPressione enter para continuar\n")
    input()

    return

