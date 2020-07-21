import random

# Função que gera X números aleatórios entre 1 e 60
def generateRandomNumbers(lim):

    vetRandNums = [] # Vetor que armazena os números aleatórios gerados

    # Executamos o loop para cada número aleatório que desejamos gerar
    for i in range(lim):
        randNum = random.randint(1, 60) # Geramos o número aleatório
        vetRandNums.append(randNum) # Salvamos o número no vetor

    # Retornamos os número aleatórios gerados
    return vetRandNums
