"""
Debuggando com PDB

PBD -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto


# A utilização do print() para debugar código é uma pratica ruim

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7,))

"""

# Existem formas mais profissionais de se fazer 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando
# o PDB - Python Debugger


# Exemplo com Pycharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7,))


# Exemplos com o PDB - Python debugger - Exemplo 1

# Para utilizar o Python Debbuger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debbuging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)


"""

# Exemplo 2

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)

Por que utilizar esse formato?

O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotexas no incio do arquivo
Por isso, ao inves de colocarmos o import do pdb no início do arquivo, nos colocamos somente onde vamos debuggar, e ao 
finalizar já fazemos a remoção


A partir do Python 3.7, não é mais necessário importar a bibliotexa pdbm pois o comando de debug foi incorporado como 
função built in (integrada) chamda breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breackpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)

"""

# Obs: Cuidado com conflitos entre nomes de variáveis e os comandos de pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel