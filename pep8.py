"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zem of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;


class Calculadora:
    pass


class calculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variáveis;


def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar= 5

[3] - Utilize 4 espaços para identação!!!! (Não usar tab)

if 'a' in 'banana':
1234print('tem') <--

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Classe:
    pass


class Outra:
    pass

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

import sys
import os

# Não há problemas em utilizar:

from types, import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda se fazer:

from types_import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça
função( algo [1], { outro: 2} )

# faça
funçao(algo[1], { outro: 2})

[7] - Termine sempre uma instrução com uma nova linha:


"""
