"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão

variável := expressão
"""

nome = 'Geek University'
print(nome)

print(nome := 'Geek University')


# Versão anteriores
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')


# Depois do Python 3.8

cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)