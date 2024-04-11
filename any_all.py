"""
Any e All

all() - Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
"""
# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False, por causa do zero

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # Todos os números são verdadeiros? True

print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? True

print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? True

print(all('Geek'))  # Todos os números são verdadeiros? True


nomes = ['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# Obs: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))


print(all([num for num in [2, 4, 10, 6, 8] if num % 2 == 0]))


"""
Any() -> Retorna True  se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna Falso
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False, se tivesse um elemento tipo 1, ja seria True

nomes = ['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))



