import random

# Função que gera X números aleatórios entre 1 e 60, sem repetições
def generateRandomNumbers(lim):

    vetRandNums = [] # Vetor que armazena os números aleatórios gerados

    # Executamos o loop para cada número aleatório que desejamos gerar
    while(lim != 0):
        randNum = random.randint(1, 60) # Geramos o número aleatório

        # Se o número aleatório não foi gerado anteriormente
        if randNum not in vetRandNums:
            vetRandNums.append(randNum) # Salvamos o número no vetor
            lim -= 1

    # Retornamos os número aleatórios gerados
    return vetRandNums

vet = generateRandomNumbers(3)
print(vet)
