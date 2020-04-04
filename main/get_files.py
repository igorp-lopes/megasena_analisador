import requests
import pathlib
import os
import datetime
from zipfile import ZipFile

rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa
# Obtemos o diretório onde os dados serão baixados
filesDir = rootDir.joinpath('files')

# Função respośavel por baixar os dados e prepara-los para o uso no programa
def obtain_data():

    databasePath = rootDir.joinpath('D_megase.zip')
    # Endereço do arquivo compactado com os dados
    url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip"

    try:
        response = requests.get(url) # Objeto obtido do request
    except Exception as erro:
        print("Algo deu errado:", erro)
    else:
        with open(databasePath, "wb") as data_zipped:
            try:
                data_zipped.write(response.content)  # Baixamos o zip na pasta files

                # Descompactamos os dados
                zipObj = ZipFile(databasePath, 'r')
                zipObj.extract('d_mega.htm', 'files')

                os.remove(databasePath) # Limpamos o diretório dos arquivos desnecessários

            except Exception as erro:
                print("Algo deu errado:", erro)

    return

# Função responsável por checar se a base de dados deve ser atualizada
def should_update():
    today = datetime.date.today() # Obtemos a data de hoje
    lastupdate_path = filesDir.joinpath('lastupdate.txt') # Localização do arquivo que registra quando ocorreu a última atualização

    try:
        
        with open(lastupdate_path, 'a+') as file:
            data_update = file.read() # Obtemos do arquivo txt a data da última atualização

            # Caso não haja registro da última atualização
            if data_update == '':
                data_update = today
                temp = data_update.strftime("%d/%m/%Y,")
                file.write(temp) # Salvamos em um arquivo txt a data atual como a data da última atualização
            else:
                data_update = data_update.strftime("%d/%m/%Y,")

            days_since_update = (today - data_update).days # Calculamos a diferença de tempo da última atualização para o dia atual                
                    

    except Exception as erro:
        print('Ouve um erro ao conferir a data da última atualização, você pode atualizar os dado manualmente no programa')
        print(f'Erro: {erro}')
        print('Prosseguindo para o programa')

    return

    

