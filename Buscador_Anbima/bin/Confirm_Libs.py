import importlib
import subprocess
import sys

def import_libraries():
    # lista de bibliotecas que precisam ser instaladas
    libs_to_install = ['pandas', 'bs4', 'unidecode']

    # verifica se o módulo pip está instalado
    try:
        importlib.import_module('pip')
    except ImportError:
        # se o módulo pip não estiver instalado, instala o pip
        import urllib.request
        url = 'https://bootstrap.pypa.io/get-pip.py'
        filename = 'get-pip.py'
        urllib.request.urlretrieve(url, filename)
        subprocess.check_call([sys.executable, filename, '--user'])
    
    # instala as bibliotecas necessárias
    for lib in libs_to_install:
        try:
            importlib.import_module(lib)
        except ImportError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
        
    # agora que todas as bibliotecas estão instaladas, você pode importá-las normalmente
    import pandas as pd
    from bs4 import BeautifulSoup
    from unidecode import unidecode
    
    return pd, BeautifulSoup, unidecode