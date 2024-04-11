"""
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para geeae sequências numéricas, não de forma aleatória,
mas sim de maneira especificada

Formas gerais

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão , e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range (valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início espeficado pelo usuario , e passo de 1 em 1)

# Exemplo Forma 2

for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início espeficado pelo usuario , e passo espeficado pelo usuario)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (Inversa)

range(valor_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_inicio espeficado pelo usuario, e passo espeficado pelo usuario)

# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)

"""
