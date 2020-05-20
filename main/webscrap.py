from bs4 import BeautifulSoup
import pathlib


def load_page():  # Função que carrega a webpage com os dados da megasena
    rootDir = pathlib.Path.cwd()  # Obtemos o diretório principal do programa
    # Obtemos o diretório onde os dados serão baixados
    filesDir = rootDir.joinpath('files')
    # Formamos o path para o arquivo da url
    URLPath = filesDir.joinpath('d_mega.htm')

    with URLPath.open('rb') as website_url:  # Abrimos a url
        # Criamos um objeto BeautifulSoup para trabalhar com os dados da página
        soup = BeautifulSoup(website_url, 'html.parser')

    return soup
