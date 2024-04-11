"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção a aprender a ler as saídas de erros geradas pela execução do nosso código

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o
Python não reconhece como parte da linguagem

# Exemplos

1 -
def funcao:
    print('Geek University')

2 -
none = 1
def = 1

3-
return

# Exemplos NameError -> Ocorre quando uma variável ou função não foi definida

1-
print(geek)


2-
a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)


# TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplos de TypeError

1-
print(len(5))

2 -
print('Geek' + [])


# IndexError -> Ocorre quando tentamos aceesar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido

# Exemplos de IndexError

1 -
lista = ['Geek']
print(lista[2])


2 -
lista = ['Geek']
print(lista[0][10])


# ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado


# Exemplos de ValueError

1 -
print(int('Geek'))

2 -
print(float('Geek'))


# KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos de KeyError

1 -
dic = {}
print(dic['geek'])


# AttributeError -> Ocorre quando uma variável não tem um atributo/função

# Exemplos de AttributeError

1 -
tupla = (11, 2, 31, 4)
print(tupla.sort())


# IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos de IndentationError

1 -
def nova():
print('Geek')

2 -
for i in range(10):
i + 1

Obs: Exceptions e Erros são sinônimos na programação

Obs: Importante ler e prestar atenção na saída de erro.
"""
