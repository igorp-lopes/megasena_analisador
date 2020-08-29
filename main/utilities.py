import os
from time import sleep

# Função que exibe o cabeçalho


def displayHeader():
    # Limpa o terminal e mostra o cabeçalho
    os.system('clear')

    print("\t**********************************************")
    print("\t***        Analisador Mega Sena            ***")
    print("\t**********************************************")
    print("\n")

    return


# Função que testa se a entrada é válida


def testValidInput(first_opt, last_opt, errorMessage = "\nComando inválido, Tente novamente\n"):

    try:
        command = int(input())  # Recebemos o comando do cmd
        # Testamos se o comando é válido
        assert(first_opt <= command <= last_opt)
    except:
        print(errorMessage)
        sleep(1.5)  # Aguardamos 3 segundos para que o texto possa ser lido
        return ""

    return command