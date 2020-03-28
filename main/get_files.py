import requests
import pathlib

rootDir = pathlib.Path.cwd() # Obtemos o diretório principal do programa

filesDir = rootDir.joinpath('files', "D_megase.zip") # Obtemos o diretório onde os dados serão baixados

#print(f'\n{filesDir}\n')

url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip" # Endereço do arquivo compactado com os dados

response = requests.get(url) # Objeto obtido do request

with open(filesDir, "wb") as data_zipped:
    data_zipped.write(response.content) # Baixamos o zip na pasta files