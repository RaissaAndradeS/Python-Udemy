"""
Tipo String

Já vimos que Python um dados é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42,3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42,3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# nome = 3'Angelina
# Jolie 3'
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

nome = 'Geek University'
print(nome.lower())

nome = 'Geek University'
print(nome.split())   # Tranforma em uma lista de strings

"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42,3"""

# àspas simples é a mais comum

# [ 0,   1,    2,  3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', '  ' 'U', 'n', 'i', 'v'  'e', 'r', 's', 'i', 't', 'y' ]
nome = 'Geek University'
print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

#  [0,         1         ]
#  ['Geek',  'University']
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])

"""
[::-1] -> Comece do primeiro elemento, vá até p último elemento e inverta 
"""
print(nome[::-1])  #Inversão da String Pythônico

print(nome.replace('G', 'P'))  # Substituir letras

texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])