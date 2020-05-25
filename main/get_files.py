import requests
import pathlib
import os
import datetime
from time import sleep
from zipfile import ZipFile
from utilities import displayHeader

rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa
# Obtemos o diretório onde os dados serão baixados
filesDir = rootDir.joinpath('files')

# Função respośavel por baixar os dados e prepara-los para o uso no programa


def obtainData():

    databasePath = rootDir.joinpath('D_megase.zip')
    # Endereço do arquivo compactado com os dados
    url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip"

    displayHeader()  # Exibimos o cabeçalho
    print("O programa está atualizando a base de dados, por favor aguarde")

    try:
        response = requests.get(url)  # Objeto obtido do request
    except Exception as erro:
        print("Algo deu errado:", erro)
    else:
        with open(databasePath, "wb") as dataZipped:
            try:
                # Baixamos o zip na pasta files
                dataZipped.write(response.content)

                # Descompactamos os dados
                zipObj = ZipFile(databasePath, 'r')
                zipObj.extract('d_mega.htm', 'files')

                # Limpamos o diretório dos arquivos desnecessários
                os.remove(databasePath)

            except Exception as erro:
                print("Algo deu errado:", erro)

    return

# Função responsável por checar se a base de dados deve ser atualizada


def should_update():
    today = datetime.date.today()  # Obtemos a data de hoje
    # Localização do arquivo que registra quando ocorreu a última atualização
    lastupdatePath = filesDir.joinpath('lastupdate.txt')
    displayHeader()  # Exibimos o cabeçalho

    try:

        with open(lastupdatePath, 'r+') as file:
            dataUpdate = file.read()  # Obtemos do arquivo txt a data da última atualização

            # Convertemos a data em string para datetime
            dataUpdate = datetime.datetime.strptime(
                dataUpdate, "%d/%m/%Y,").date()

            # Calculamos a diferença de tempo da última atualização para o dia atual
            daysSinceUpdate = (today - dataUpdate).days

            if daysSinceUpdate > 7:  # Testamos se a última atualização foi a mais de 7 dias

                while(True):

                    try:
                        displayHeader()  # Exibimos o cabeçalho
                        print(
                            f"O banco de dados foi atualizado pela última vez há {daysSinceUpdate} dias")
                        print("Gostaria de atualiza-lo?")
                        print('(1) - Sim\n(2) - Não')
                        command = input()
                        assert((command == '1') or (command == '2'))
                    except:
                        print('Comando inválido, tente novamente')
                        sleep(1.5)
                    else:
                        break

                if command == '1':  # Caso queiramos atualizar
                    obtainData()  # Atualizamos o banco de dados
                    # Convertemos a data para o formato de string
                    today = today.strftime("%d/%m/%Y,")
                    file.seek(0)
                    file.truncate(0)  # Apagamos o conteúdo do arquivo
                    # Salvamos em um arquivo txt a data atual como a data da última atualiza
                    file.write(today)

                print("Pressione enter para continuar\n")
                input()

    except IOError as erro:  # Caso no qual não há arquivo com a data da última atualização

        print('\nNão foi possível determinar a data da última atualização')
        print('O programa vai atualizar o banco de dados agora')
        print("Pressione enter para continuar\n")
        input()
        try:

            with open(lastupdatePath, 'w') as file:
                # Convertemos para string a data do dia atual
                temp = today.strftime("%d/%m/%Y,")
                # Salvamos em um arquivo txt a data atual como a data da última atualização
                file.write(temp)

        except Exception as erro:
            print('Ocorreu um erro ao salvar a data de atualização')
            print(f'Erro: {erro}')
            print('Prosseguindo para o programa')

        obtainData()  # Atualizamos o banco de dados

    except Exception as erro:
        print('Ocorreu um erro no processo de verificação da atualização')
        print(f'Erro: {erro}')
        print('Prosseguindo para o programa')

    return
