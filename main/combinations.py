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

    numErrMes = "\nNúmero inválido, tente novamente\n" # Mensagem de erro especial para número inválido

    while(True):
        displayHeader()
        print("Digite quantos números aleatórios você quer na combinação (máximo 20)")

        # Testamos se o número da entrada é válido
        totComb = testValidInput(1,20, numErrMes)

        # Se a entrada é válida
        if(totComb):
            break

    randNums = generateRandomNumbers(totComb) # Gereamos os números aleatórios

    # Exibimos ao usuários os números gerados
    displayHeader()
    print("Os números aleatórios gerados foram:\n")
    print(randNums)
    print("\nPressione enter para continuar")

    input()

    return


