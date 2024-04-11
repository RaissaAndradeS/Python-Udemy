"""
Try / Except / Else / Finally

TODA ENTRADA DEVE SER TRATADA

Obs: A função do usuário é DESTRUIR seu sistema


# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}')

"""

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

print('Depois do bloco try/except')

# OBS: o bloco finally é sempre executado. Independente se houve exceção ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.


"""

# Exemplo mais complexo

def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
    
"""

# Exemplo mais complexo correto

# Obs: Você é responsável pelas entradas das suas funções. Então, trate


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Outra forma 

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))