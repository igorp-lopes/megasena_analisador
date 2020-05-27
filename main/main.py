import get_files
import webscrap
import analysis
from utilities import displayHeader, testValidInput


## FUNÇÔES ##

# Função que implementa a interface central


def mainInterface():

    # Função que exibe o menu principal
    def displayMenu():

        displayHeader()  # Mostramos o cabeçalho
        print("Bem vindo ao analisador de jogos da Mega Sena!")
        print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")
        print("(1) - Análisar resultados")
        print("(2) - Atualizar banco de dados")
        print("(3) - Sair")

        return

    while(True):
        
        get_files.should_update() # Avaliamos se a base de dados deve ser atualizada
        displayMenu()
        command = testValidInput(1, 3)

        if command == 1:
            analysisMenu()  # Vamos para o menu de análises
        elif command == 2:
            get_files.obtainData()  # Baixamos os dados mais recentes

        elif command == 3:
            break

    return

# Função que implementa a interface de análise


def analysisMenu():

    def displayMenu():

        displayHeader()  # Exibimos o cabeçalho

        print("(1) - Análisar a recorrência dos números")
        print("(2) - Voltar")

        return

    get_files.should_update()
    displayHeader() 
    # Criamos o dataframe através dos dados baixados

    dataframe = analysis.selectDateInterval(webscrap.extractData(), 1, 0)
    while(True):

        displayMenu()
        command = testValidInput(1, 2)

        if command == 1:
            recurrencyMenu(dataframe)
        elif command == 2:
            break

    return

# Função que implementa o menu de análise de recorrência


def recurrencyMenu(dataframe):

    def displayMenu():

        displayHeader()  # Exibimos o cabeçalho

        print("(1) - Exibir os 6 números mais sorteados")
        print("(2) - Exibir os 6 números menos sorteados")
        print("(3) - Ver a recorrência de um número específico")
        print("(4) - Voltar")

        return

    while(True):
        displayMenu()
        command = testValidInput(1, 4)

        if command == 1:
            analysis.findRecurrency('mais frequentes', dataframe)
        elif command == 2:
            analysis.findRecurrency('menos frequentes', dataframe)
        elif command == 3:
            analysis.findRecurrency('Specific Number', dataframe)
        elif command == 4:
            break

## PROGRAMA ##


mainInterface()
