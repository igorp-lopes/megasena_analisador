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
    
    tempDf = pd.read_html(str(table)) # Transformamos a tabela em um dataframe

    dfTable = tempDf[0]

    # Limpamos os dados da tabela fazendo os ajustes necessários

    # Armazenamos apenas as colunas da tabela que nos interessam
    df = dfTable[ ["Concurso", 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', 
    '6ª Dezena', 'Ganhadores_Sena', 'Rateio_Sena', 'Acumulado', 'Valor_Acumulado']]

    # Alteramos o nome de algumas colunas
    df.rename(columns={'Ganhadores_Sena': 'Número de Ganhadores', 'Valor_Acumulado': 'Valor Acumulado', 'Rateio_Sena': 'Rateio'}, inplace=True)

    df['Data Sorteio']= pd.to_datetime(df['Data Sorteio'], infer_datetime_format = True) # Passamos os dados da coluna das datas para o tipo datetime
    
    return df # Retornamos o dataframe com a tabela de dados