import get_files
import webscrap
import analysis
from utilities import display_header, test_valid_input


## FUNÇÔES ##

# Função que implementa a interface central


def main_interface():

    # Função que exibe o menu principal
    def display_menu():

        display_header()  # Mostramos o cabeçalho
        print("Bem vindo ao analisador de jogos da Mega Sena!")
        print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")
        print("(1) - Análisar resultados")
        print("(2) - Atualizar banco de dados")
        print("(3) - Sair")

        return

    while(True):

        display_menu()
        command = test_valid_input(1, 3)

        if command == 1:
            analysis_menu()  # Vamos para o menu de análises
        elif command == 2:
            get_files.obtain_data()  # Baixamos os dados mais recentes

        elif command == 3:
            break

    return

# Função que implementa a interface de análise


def analysis_menu():

    def display_menu():

        display_header()  # Exibimos o cabeçalho

        print("(1) - Análisar a recorrência dos números")
        print("(2) - Voltar")

        return

    # Criamos o dataframe através dos dados baixados
    dataframe = webscrap.extract_data()
    while(True):

        display_menu()
        command = test_valid_input(1, 2)

        if command == 1:
            recurrency_menu(dataframe)
        elif command == 2:
            break

    return

# Função que implementa o menu de análise de recorrência


def recurrency_menu(dataframe):

    def display_menu():

        display_header()  # Exibimos o cabeçalho

        print("(1) - Exibir os 6 números mais sorteados")
        print("(2) - Exibir os 6 números menos sorteados")
        print("(3) - Ver a recorrência de um número específico")
        print("(4) - Voltar")

        return

    while(True):
        display_menu()
        command = test_valid_input(1, 4)

        if command == 1:
            analysis.find_recurrency('mais frequentes', dataframe)
        elif command == 2:
            analysis.find_recurrency('menos frequentes', dataframe)
        elif command == 3:
            analysis.find_recurrency('Specific Number', dataframe)
        elif command == 4:
            break

## PROGRAMA ##


main_interface()
