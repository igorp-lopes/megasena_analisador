from bs4 import BeautifulSoup
import os
import numpy as np
import pandas as pd

print("Bem vindo ao analisador de jogos da Mega Sena!")
print("Para acessar a funcionalidade desejada, digite o número da opção e confirme com a tecla 'enter'\n")

while(True):
    print("(1) - Obter frequência de certo número")
    print("(2) - Atualizar banco de dados")
    print("(3) - Ajuda")
    print("(4) - Sair")

    command = int(input()) # Recebemos o comando do cmd
