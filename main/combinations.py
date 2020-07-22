import random
from time import sleep
from utilities import displayHeader, testValidInput

# Função que gera X números aleatórios entre 1 e 60, sem repetições
def generateRandomNumbers(total):

    vetRandNums = [] # Vetor que armazena os números aleatórios gerados

    # Executamos o loop para cada número aleatório que desejamos gerar
    while(total != 0):
        randNum = random.randint(1, 60) # Geramos o número aleatório

        # Se o número aleatório não foi gerado anteriormente
        if randNum not in vetRandNums:
            vetRandNums.append(randNum) # Salvamos o número no vetor
            total -= 1

    # Retornamos os número aleatórios gerados
    return vetRandNums

# Função que gera uma combinação de 6 números aleatórios para mega sena
def randomComb():

    while(True):
        displayHeader()
        print("Digite quantos números aleatórios você quer na combinação (máximo 20)")


        try:
            totComb = int(input()) # Recebemos quantos número aleatórios devemos gerar
            assert(totComb <= 20) # Testamos se o valor recebido é válido

            randNums = generateRandomNumbers(totComb) # Gereamos os números aleatórios
            break
            
        except:
            print("\nNúmero inválido, tente novamente\n")
            sleep(1.5)  # Aguardamos 3 segundos para que o texto possa ser lido

    # Exibimos ao usuários os números gerados
    displayHeader()
    print("Os números aleatórios gerados foram:\n")
    print(randNums)
    print("\nPressione enter para continuar")

    input()

    return




