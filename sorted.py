"""
Sorted

OBS: Não confunda com a função sort() que já estudamos em Listas. O sort() só funciona em listas

Podemos utilizar o sorted com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar

Obs: O sorted SEMPRE retorna uma Lista como os elementos do iterável ordendos
"""

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)


# Adicionando parâmetros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True))   #Ordena do maior para o menor



# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32},
]

# Ordena da menos tocada para mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))






