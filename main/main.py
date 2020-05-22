import get_files
import os
from time import sleep

def main_interface():

    def display_menu():
        # Limpa o terminal e mostra o menu principal
        os.system('clear')
              
        print("\t**********************************************")
        print("\t***        Analisador Mega Sena            ***")
        print("\t**********************************************")

        print("\nBem vindo ao analisador de jogos da Mega Sena!")

        print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")

        print("(1) - Obter frequência de certo número")
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
            sleep(3)
        else:
            if command == 1:
                pass
            elif command == 2:
                get_files.obtain_data() # Baixamos os dados mais recentes
            elif command == 3:
                pass
            else:
                break

    return

main_interface()