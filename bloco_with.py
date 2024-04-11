"""
O bloco with

Passos para se trabalhar como arquivos

1 - abrir
2 - trabalhar
3 - fechar

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with

"""

# O block with - Forma Pythônica

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


# print(arquivo.read())
print(arquivo.closed)