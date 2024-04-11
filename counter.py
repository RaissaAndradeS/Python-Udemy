"""
Módulo Collections - Counter (Contador)

Collections -> High - performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário,
contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.

"""
# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 45, 34]

# Utilizando o Counter

res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 3, 66: 2, 34: 1})

# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = """A Universidade de Brasília (UnB) anunciou a abertura de inscrições para um novo Concurso Público, 
que tem como objetivo preencher uma vaga para o cargo de Professor Adjunto A, 
com candidato com doutorado, na Faculdade do Gama."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto

print(res.most_common(5))