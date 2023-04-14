# Importa as bibliotecas necessárias
import pandas as pd 
import requests 
from bs4 import BeautifulSoup 

def coletar_dados(df):
    df2=pd.DataFrame()
    # Define a URL a ser acessada
    for url in df['Links']:
        # Faz uma requisição GET na URL e guarda o resultado na variável 'response'
        response = requests.get(url) 

        # Cria um objeto BeautifulSoup a partir do conteúdo HTML da resposta da requisição
        soup = BeautifulSoup(response.content, 'html.parser') 

        # Define variáveis para guardar os dados coletados
        assossiadodesde = ""
        titular = ""
        suplente = ""
        razao_social = ""
        cnpj = ""
        site = ""
        cpa10 = ""
        cpa20 = ""
        cfg = ""
        cga = ""
        cge = ""
        cea = ""
        cod_adm = ""
        cert_cont = ""
        prod_invest = ""
        instr_finan = ""

        # Coleta dados a partir de elementos HTML usando o método 'find' do BeautifulSoup, e guarda os valores nas variáveis correspondentes
        try:
            assossiadodesde = soup.find('h2', text='Associado desde').find_next('p').get_text().strip()
        except:
            pass

        try:
            titular = soup.find('h3', text='Titular').find_next('p').get_text().strip()
        except:
            pass

        try:
            suplente = soup.find('h3', text='Suplentes').find_next('p').get_text().strip()
        except:
            pass

        try:
            razao_social = soup.find('h2', text='Razão Social').find_next('p').get_text().strip()
        except:
            pass

        try:
            cnpj = soup.find('h2', text='CNPJ').find_next('p').get_text().strip()
        except:
            pass

        try:
            site = soup.find('h2', text='Website').find_next('a').get('href')
        except:
            pass


        try:
            cpa10 = soup.find('h3', text='CPA-10').find_next('p').find('span').get_text().strip()
        except:
            pass

        try:
            cpa20 = soup.find('h3', text='CPA-20').find_next('p').find('span').get_text().strip()
        except:
            pass

        try:
            cfg = soup.find('h3', text='CFG').find_next('p').find('span').get_text().strip()
        except:
            pass

        try:
            cga = soup.find('h3', text='CGA').find_next('p').find('span').get_text().strip()
        except:
            pass

        try:
            cge = soup.find('h3', text='CGE').find_next('p').find('span').get_text().strip()
        except:
            pass

        try:
            cea = soup.find('h3', text='CEA').find_next('p').find('span').get_text().strip()
        except:
            pass


        try:
            ul_element = soup.find('h3', text='Atividades desempenhadas no mercado').find_next('ul')
            li_elements = ul_element.find_all('li')
            
            # Itera pelos elementos li e coleta os dados
            dados = []
            for li in li_elements:
                dado = li.get_text().strip()
                dados.append(dado)
                
            # Concatena todos os dados em uma string separada por vírgula
            cod_adm = ', '.join(dados)
            
        except:
            pass

        try:
            ul_element = soup.find('h3', text='CÓDIGO PARA O PROGRAMA DE CERTIFICAÇÃO CONTINUADA').find_next('h3').find_next('ul')
            li_elements = ul_element.find_all('li')
            
            # Itera pelos elementos li e coleta os dados
            dados = []
            for li in li_elements:
                dado = li.get_text().strip()
                dados.append(dado)
                
            # Concatena todos os dados em uma string separada por vírgula
            cert_cont = ', '.join(dados)

        except:
            pass

        try:
            ul_element = soup.find('h3', text='CÓDIGO DE DISTRIBUIÇÃO DE PRODUTOS DE INVESTIMENTO').find_next('h3').find_next('ul')
            li_elements = ul_element.find_all('li')
            
            # Itera pelos elementos li e coleta os dados
            dados = []
            for li in li_elements:
                dado = li.get_text().strip()
                dados.append(dado)
                
            # Concatena todos os dados em uma string separada por vírgula
            prod_invest = ', '.join(dados)

        except:
            pass

        try:
            ul_element = soup.find('h3', text='CÓDIGO DE NEGOCIAÇÃO DE INSTRUMENTOS FINANCEIROS').find_next('h3').find_next('ul')
            li_elements = ul_element.find_all('li')
            
            # Itera pelos elementos li e coleta os dados
            dados = []
            for li in li_elements:
                dado = li.get_text().strip()
                dados.append(dado)
                
            # Concatena todos os dados em uma string separada por vírgula
            instr_finan = ', '.join(dados)

        except:
            pass
        # Cria um DataFrame vazio com as colunas de interesse
        df = pd.DataFrame({"Associado Desde": [assossiadodesde],
                           "Razão Social": [razao_social],
                           "CNPJ": [cnpj],
                           "Site": [site],
                           "Titular": [titular],
                           "Suplentes": [suplente],
                           "Recursos de Terceiros": [cod_adm],
                           "Produtos de Investimentos": [prod_invest],
                           "Instrumentos Financeiros": [instr_finan],
                           "Certificação Continuada": [cert_cont],
                           "CPA-10": [cpa10],
                           "CPA-20": [cpa20],
                           "CFG": [cfg],
                           "CGA": [cga],
                           "CGE": [cge],
                           "CEA": [cea]})

        # Imprime o DataFrame
        df2 = pd.concat([df, df2], ignore_index=True)
    df2.to_excel('archives/results/DadosAnbima.xlsx', index=False)
    print(df2)
