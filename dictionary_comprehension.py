"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4)  # 1, 2, 3, 4

conjunto = {1, 2, 3, 4}

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{chave: valor for valor in iterável}
[valor for valor in iteravel] lista

"""
# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# Ex
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# Ex

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)



