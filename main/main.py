import get_files
import os
from time import sleep

## FUNÇÔES ##

# Função que exibe o cabeçalho


def display_header():
    # Limpa o terminal e mostra o cabeçalho
    os.system('clear')

    print("\t**********************************************")
    print("\t***        Analisador Mega Sena            ***")
    print("\t**********************************************")
    print("\n")

    return

# Função que implementa a interface central


def main_interface():

    # Função que exibe o menu principal
    def display_menu():

        display_header()  # Mostramos o cabeçalho
        print("Bem vindo ao analisador de jogos da Mega Sena!")
        print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")
        print("(1) - Análisar resultados")
        print("(2) - Atualizar banco de dados")
        print("(3) - Ajuda")
        print("(4) - Sair")

        return

    while(True):

        display_menu()
        command = int(input())  # Recebemos o comando do cmd

        try:
            assert(1 <= command <= 4)  # Testamos se o comando é válido
        except:
            print("\nComando inválido, Tente novamente\n")
            sleep(3)  # Aguardamos 3 segundos para que o texto possa ser lido
        else:
            if command == 1:
                analysis_menu()  # Vamos para o menu de análises
            elif command == 2:
                get_files.obtain_data()  # Baixamos os dados mais recentes
            elif command == 3:
                pass
            else:
                break

    return

# Função que implementa a interface de análise


def analysis_menu():

    def display_menu():

        display_header()  # Exibimos o cabeçalho

        print("(1) - Análisar a recorrência dos números")
        print("(2) - Voltar")

        return

    while(True):

        display_menu()
        command = int(input())  # Recebemos o comando do cmd

        try:
            assert(1 <= command <= 2)  # Testamos se o comando é válido
        except:
            print("\nComando inválido, Tente novamente\n")
            sleep(3)  # Aguardamos 3 segundos para que o texto possa ser lido
        else:
            if command == 1:
                recurrency_menu()
            else:
                break

    return


def recurrency_menu():

    def display_menu():

        display_header()  # Exibimos o cabeçalho

        print("(1) - Exibir os 6 números mais sorteados")
        print("(2) - Exibir os 6 números menos sorteados")
        print("(3) - Ver a recorrência de um número específico")
        print("(4) - Voltar")

        return

    while(True):
        display_menu()
        command = int(input())  # Recebemos o comando do cmd

        try:
            assert(1 <= command <= 4)  # Testamos se o comando é válido
        except:
            print("\nComando inválido, Tente novamente\n")
            sleep(3)  # Aguardamos 3 segundos para que o texto possa ser lido
        else:
            if command == 1:
                pass
            elif command == 2:
                pass
            elif command == 3:
                pass
            else:
                break

## PROGRAMA ##


main_interface()
