"""
Funções como retorno

OBS: Em python, quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções
"""
numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# Segunda não retorna nada

# Exemplo função

def quadrado_de_7():
    print(7 * 7)

quadrado_de_7()

# Retornar é diferente de imprimir

ret = quadrado_de_7()

print(f'Retorno {ret}')


# Refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função

ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Operação

print(f'Retorno: {quadrado_de_7() + 1}')


# Refatorando a primeira função

def diz_oi():
    return 'Oi! '

print(diz_oi())

alguem = 'Pedro'

print(diz_oi() + alguem)

# OBS: Sobre a palavra reservada return
# 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
# 2 - Podemos ter, em uma função, diferentes returns;
# 3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo múltipos valores;

# Exemplo 1

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())

# Exemplo 2

def nova_funcao():
    variavel = True    #(Testes /None/False)
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

# Modo 1
num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# Modo 2 tupla
print(outra_funcao())
print(type(outra_funcao()))


# Vamos criar uma função para jogar moeda

from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


# Erros comuns na utilização do retorno, "codificação desnecessária"

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())

# Não precisa do Else 