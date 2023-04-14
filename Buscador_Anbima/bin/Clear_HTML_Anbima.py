import os
import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode

def extrair_dados_html(file_path):
    # Abre o arquivo e lê o conteúdo
    with open(file_path, 'r') as file:
        html = file.read()

    # Cria um objeto BeautifulSoup a partir do HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra todas as tags 'div' com a classe 'card-associado'
    card_divs = soup.find_all('div', class_='card-associado')

    # Cria uma lista vazia para armazenar os dados extraídos
    dados = []

    # Itera sobre as tags 'div'
    for div in card_divs:
        # Encontra a tag 'a'
        a_tag = div.find('a')

        # Extrai o link (href) da tag 'a'
        link = a_tag.get('href')

        # Encontra a tag 'h4'
        h4_tag = div.find('h4')

        # Extrai o texto da tag 'h4'
        text = h4_tag.text

        # Extrai o id do link
        id = link.split('=')[-1]

        # Adiciona os dados extraídos à lista
        dados.append({'Texto': text, 'ID': id})

    # Cria um DataFrame a partir da lista de dados
    df = pd.DataFrame(dados)
    # Aplicar as transformações
    tabela = str.maketrans('', '', '.,/()')
    df = df.applymap(lambda x: unidecode(x.lower().replace(' ', '-')).translate(tabela))
    
    return df

def gerar_links_excel(df):
    links = pd.DataFrame()
    links['link'] = 'https://www.anbima.com.br/pt_br/institucional/perfil-da-instituicao/instituicao/' + df['ID'] + '/perfil/' + df['Texto'] + '.htm'
    links['link'].to_excel('archives/results/links.xlsx', index=False)

