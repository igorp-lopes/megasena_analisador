def main_interface():

    print("Bem vindo ao analisador de jogos da Mega Sena!")

    print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")

    while(True):
        print("(1) - Obter frequência de certo número")
        print("(2) - Atualizar banco de dados")
        print("(3) - Ajuda")
        print("(4) - Sair")

        command = int(input())  # Recebemos o comando do cmd

        try:
            assert(1 <= command <= 4)  # Testamos se o comando é válido
        except:
            print("\nComando inválido, Tente novamente\n")
        else:
            if command == 1:
                pass
            elif command == 2:
                pass
            elif command == 3:
                pass
            else:
                break

    return

main_interface()