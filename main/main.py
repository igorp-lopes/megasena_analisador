import get_files
import webscrap
import analysis
from time import sleep
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
        print("(3) - Gerar combinações")
        print("(4) - Sair")

        return

    while(True):
        
        displayMenu()
        command = testValidInput(1, 4)

        if command == 1:
            analysisMenu()  # Vamos para o menu de análises
        elif command == 2:
            get_files.obtainData()  # Baixamos os dados mais recentes

        elif command == 3:
            combinationsMenu() # Vamos para o menu de combinações

        elif command == 4:
            break

    return

# Função que implementa a interface de formação de combinações
def combinationsMenu():

    # Função que exibe o menu principal
    def displayMenu():

        displayHeader()  # Mostramos o cabeçalho
        print("(1) - Combinações aleatórias")
        print("(2) - Combinações com números específicos")
        print("(3) - Voltar ")

        return

    while(True):

        displayMenu()
        command = testValidInput(1, 3)

        if command == 1:
            pass

        elif command == 2:
            pass

        elif command == 3:
            break

# Função que implementa o menu de seleção do tipo de intervalo de datas para realizar a análise
def selectDateInterval():
    
    def displayMenu():

        displayHeader()  # Exibimos o cabeçalho

        print("Selecione o intervalo de tempo dos dados a serem analisados")
        print("De hoje até 'X' meses/anos atrás")

        print("(1) - Selecionar a data em meses")
        print("(2) - Selecionar a data em anos")
        print("(3) - Voltar")

        return

    multiplicador = 1 # Variável que ajusta o intervalo de tempo para meses ou anos

    while(True):

        displayMenu()
        command = testValidInput(1, 2)

        if command == 1:
            multiplicador = 1
            tipoIntervalo = 'meses'
            break

        elif command == 2:
            multiplicador = 12
            tipoIntervalo = 'anos'
            break

    while(True):

        displayHeader()
        print(f"Selecione de hoje até quantos {tipoIntervalo} atrás devem ser os dados a serem analisados:")
        print("Se deseja analisar os dados desde o começo digite um número negativo")

        valor = input() # Recebemos o comando do cmd

        # Testamos se o valor colocado é válido, ignorando o possível sinal negativo '-'
        if (valor.strip('-')).isnumeric():
            return int(valor) * multiplicador # Retornamos o tamanho do intervalo, aplicado a conversão se necessário

        else:
            print("\nComando inválido, Tente novamente\n")
            sleep(1.5)  # Aguardamos 3 segundos para que o texto possa ser lido
    

# Função que implementa a interface de análise


def analysisMenu():

    def displayMenu():

        displayHeader()  # Exibimos o cabeçalho

        print("(1) - Análisar a recorrência dos números")
        print("(2) - Relacionar ocorrências com datas")
        print("(3) - Voltar")

        return

    get_files.should_update()

    intervaloDatas = selectDateInterval() # Selecionamos o intervalo dos dados a serem considerados
    displayHeader() 

    print("O programa está carregando a base de dados, por favor aguarde")
    # Criamos o dataframe através dos dados baixados
    dataframe = webscrap.extractData()

    # Se desejamos escolher um intervalo específico de tempo dos dados
    if intervaloDatas > 0:
        dataframe = analysis.selectDateInterval(dataframe, intervaloDatas)

    while(True):

        displayMenu()
        command = testValidInput(1, 3)

        if command == 1:
            recurrencyMenu(dataframe)
        elif command == 2:
            dateMenu(dataframe)
        elif command == 3:
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


# Função que implementa o menu de análise data - ocorrencias


def dateMenu(dataframe):

    def displayMenu():

        displayHeader()  # Exibimos o cabeçalho

        print("(1) - Análise de data - ocorrências para um número especifico")
        print("(2) - Ordenar os números pela última vez em que eles ocorreram")
        print("(3) - Ordenar os números pela primeira vez em que eles ocorreram")
        print("(4) - Voltar")

        return

    while(True):
        displayMenu()
        command = testValidInput(1, 4)

        if command == 1:
            analysis.dateAnalysis("Specific Number",dataframe)
        elif command == 2:
            analysis.dateAnalysis("Most Recent", dataframe)
        elif command == 3:
            analysis.dateAnalysis("Oldest", dataframe)
        elif command == 4:
            break

## PROGRAMA ##


mainInterface()
