"""
Criando sua propria versão de loop

iter([1, 2, 3, 4, 5, 6])

iter('Geek University')
"""

for num in [1, 2, 3, 4, 5,]:
    print(num)

for letra in 'Geek University':
    print(letra)


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')


numeros = [1, 2, 3, 4, 5]

meu_for(numeros)