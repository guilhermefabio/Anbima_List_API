import os
import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode

def extrair_dados_html(file_path):
    # Abre o arquivo e lê o conteúdo
    with open(file_path, 'r', encoding="utf-8") as file:
        html = file.read()

    # Cria um objeto BeautifulSoup a partir do HTML lido
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra todas as tags <a> que contêm o atributo href
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        href = href.replace('../../', 'https://www.anbima.com.br/')
        links.append(href)

    # Cria um dataframe com os links encontrados
    df = pd.DataFrame(links, columns=['Links'])

    # Exibe o dataframe
    print(df)

    return df

def gerar_links_excel(df):
    links = pd.DataFrame(df)
    links.to_excel('archives/results/links.xlsx', index=False)
    return links

