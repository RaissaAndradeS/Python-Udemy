"""
Filter

Filter() -> Serve para filtrar dados de uma determinada coleção

"""

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

# Biblioteca para trabalhar com dados estatísticos

import statistics

# dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim xomo a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x > media, dados)   # Retorna True ou False
print(type(res))
print(list(res))

print(f'Novamente: {list(res)}')  # Some da memoria, como Map

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)

res = filter(lambda pais: pais != '', paises)


print(list(res))


# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iteravél e retorna um objeto filtrando apenas os elementos de acordo com a função

# Map -> valores, filter-> booleanos, True of False


# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtras os usuários que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

print(inativos)

# Refatorando

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

# Combinar filter() e map ()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)


