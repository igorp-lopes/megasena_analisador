from bs4 import BeautifulSoup
import pathlib
import pandas as pd

def loadPage():  # Função que carrega a webpage com os dados da megasena
    rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa
    # Obtemos o diretório onde os dados serão baixados
    filesDir = rootDir.joinpath('files')
    # Formamos o path para o arquivo da url
    URLPath = filesDir.joinpath('d_mega.htm')

    with URLPath.open('rb') as websiteUrl:  # Abrimos a url
        # Criamos um objeto BeautifulSoup para trabalhar com os dados da página
        soup = BeautifulSoup(websiteUrl, 'html.parser')

    return soup


def extractData(): # Função que extrai os dados da webpage

    
    website = loadPage() # Carregamos a webpage com os dados
    table = website.find('table') # Separamos a tabela da página
    
    tempDf = pd.read_html(str(table), skiprows = [i for i in range(7,21)]) # Transformamos a tabela em um dataframe

    dfTable = tempDf[0]

    # Limpamos os dados da tabela fazendo os ajustes necessários

    # Armazenamos apenas as colunas da tabela que nos interessam
    df = dfTable[ ["Concurso", 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', 
    '6ª Dezena']]


    df['Data Sorteio']= pd.to_datetime(df['Data Sorteio'], format = '%d/%m/%Y') # Passamos os dados da coluna das datas para o tipo datetime
    df['Data Sorteio'] = df['Data Sorteio'].dt.date # Guardamos apenas a parte das datas do tipo datetime
    
    return df # Retornamos o dataframe com a tabela de dados