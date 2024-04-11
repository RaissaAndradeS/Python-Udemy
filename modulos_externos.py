"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.prg

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Fore: cor da letra

Back: cor de fundo

Installando um módulo: pip install nome-do-modulo

from colorama import init, Fore, Back

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Back.RED + 'Hello')

"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)