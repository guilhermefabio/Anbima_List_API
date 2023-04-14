import sys
import os

# adiciona o caminho da pasta bin ao path
sys.path.append(os.path.abspath('bin'))

# importa a função do arquivo Clear_HTML_Anbima.py
from Clear_HTML_Anbima import *
from Confirm_Libs import *


if __name__ == '__main__':
	import_libraries()
	app_banner  = '\nBusca Anbima\' | GNU License (C) 2023 | Guilherme Vieira & Airton Warmling\n'
	print(app_banner)
	print('===========================================================================\n')
	print("""  ______          _                                                  
 |___  /         (_)                                                 
    / /_   _ _ __ _                                                  
   / /| | | | '__| |                                                 
  / /_| |_| | |  | |                                                 
 /_____\__,_|_|  |_|                         _     _                 
 |  _ \                          /\         | |   (_)                
 | |_) |_   _ ___  ___ __ _     /  \   _ __ | |__  _ _ __ ___   __ _ 
 |  _ <| | | / __|/ __/ _` |   / /\ \ | '_ \| '_ \| | '_ ` _ \ / _` |
 | |_) | |_| \__ | (_| (_| |  / ____ \| | | | |_) | | | | | | | (_| |
 |____/ \__,_|___/\___\__,_| /_/    \_|_| |_|_.__/|_|_| |_| |_|\__,_|
                                                                     
                                                                     \n""")
	# Caminho do arquivo HTML que será lido

	file_path = os.path.expanduser("archives/objects/Estrutura_HTML_14042023.html")
	# Extrai os dados do arquivo HTML
	df = extrair_dados_html(file_path)
	# Gera o arquivo de links
	gerar_links_excel(df)
	print("Concluido......")
