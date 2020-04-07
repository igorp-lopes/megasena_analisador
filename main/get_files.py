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
        response = requests.get(url)  # Objeto obtido do request
    except Exception as erro:
        print("Algo deu errado:", erro)
    else:
        with open(databasePath, "wb") as data_zipped:
            try:
                # Baixamos o zip na pasta files
                data_zipped.write(response.content)

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
    lastupdate_path = filesDir.joinpath('lastupdate.txt')

    try:

        with open(lastupdate_path, 'r+') as file:
            data_update = file.read()  # Obtemos do arquivo txt a data da última atualização

            # Convertemos a data em string para datetime
            data_update = datetime.datetime.strptime(
                data_update, "%d/%m/%Y,").date()

            # Calculamos a diferença de tempo da última atualização para o dia atual
            days_since_update = (data_update - today).days

            if days_since_update > 7:  # Testamos se a última atualização foi a mais de 7 dias
                print(
                    f"O banco de dados foi atualizado pela última vez há {days_since_update} dias")
                print("Gostaria de atualiza-lo?")

                while(True):

                    try:
                        print('(1) - Sim\n(2) - Não')
                        command = input()
                        assert((command == '1') or (command == '2'))
                    except:
                        print('Comando inválido, tente novamente')
                    else:
                        break

                if command == '1':  # Caso queiramos atualizar
                    obtain_data()  # Atualizamos o banco de dados
                    # Convertemos a data para o formato de string
                    today = today.strftime("%d/%m/%Y,")
                    file.seek(0)
                    file.truncate(0)  # Apagamos o conteúdo do arquivo
                    # Salvamos em um arquivo txt a data atual como a data da última atualiza
                    file.write(today)

    except IOError as erro:  # Caso no qual não há arquivo com a data da última atualização

        print('\nNão foi possível determinar a data da última atualização')
        print('O programa vai atualizar o banco de dados agora')
        try:

            with open(lastupdate_path, 'w') as file:
                # Convertemos para string a data do dia atual
                temp = today.strftime("%d/%m/%Y,")
                # Salvamos em um arquivo txt a data atual como a data da última atualização
                file.write(temp)

        except Exception as erro:
            print('Ocorreu um erro ao salvar a data de atualização')
            print(f'Erro: {erro}')
            print('Prosseguindo para o programa')

        obtain_data()  # Atualizamos o banco de dados

    except Exception as erro:
        print('Ocorreu um erro no processo de verificação da atualização')
        print(f'Erro: {erro}')
        print('Prosseguindo para o programa')

    return
