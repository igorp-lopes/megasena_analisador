import requests
import pathlib
import os
from zipfile import ZipFile


def obtain_data():

    rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa

    # Obtemos o diretório onde os dados serão baixados
    filesDir = rootDir.joinpath('files', "D_megase.zip")
    # Endereço do arquivo compactado com os dados
    url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip"

    response = requests.get(url)  # Objeto obtido do request

    with open(filesDir, "wb") as data_zipped:
        data_zipped.write(response.content)  # Baixamos o zip na pasta files

        # Descompactamos os dados
        zipObj = ZipFile(filesDir, 'r')
        zipObj.extract('d_mega.htm', 'files')

    os.remove(filesDir) # Limpamos o diretório dos arquivos desnecessários

    return
