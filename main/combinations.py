import random
from time import sleep
from itertools import combinations
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
        if totComb:
            break

    randNums = generateRandomNumbers(totComb) # Gereamos os números aleatórios

    # Exibimos ao usuários os números gerados
    displayHeader()
    print("Os números aleatórios gerados foram:\n")
    print(randNums)
    print("\nPressione enter para continuar")

    input()

    return

# Função que gera uma combinação de X números Y a Y definidos pelo usuário
def userDefComb():

    numErrMes = "\nNúmero inválido, tente novamente\n" # Mensagem de erro especial para número inválido

    while(True):
        displayHeader()
        print("Digite quantos números você quer na combinação (máximo 20)")

        # Recebemos com quantos números desejamos realizar a combinação
        totNums = testValidInput(1,20, numErrMes)

        # Se a entrada é válida
        if totNums:
            break

    # Recebemos os números com os quais se deseja fazer as combinações
    vetNums = [] # Vetor que salva os números que serão usados nas combinações
    i = 0 # Contador

    while(totNums > i):
        displayHeader()
        print("Entre com os números que deseja usar nas combinações:")

        # Recebemos o número para fazer a combinação
        num = testValidInput(0, 60, numErrMes)

        # Se a entrada é válida
        if num:
            vetNums.append(num) # Salvamos o número no vetor
            i += 1 # Incrementamos o contador

    
    while(True):
        displayHeader()
        print("Digite de quanto a quanto você deseja fazer a combinação, um por vez: ")

        # Testamos se o número da entrada é válido
        parComb = testValidInput(1, totNums, numErrMes)

        # Se a entrada é válida
        if(parComb):
            break

    # Obtemos as combinações
    combs = list(combinations(vetNums, parComb))

    # Printamos as combinações geradas
    print("\nAs combinações com os números selecionados são as seguintes:\n")
    for comb in combs: 
        print(comb)

    print("\nPressione enter para continuar")
    input()

    return

