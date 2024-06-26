"""
Tipo Booleano

Álgebra Booleana, verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula
# Certo
True/False
"""
ativo = False
print(ativo)


"""
Operações básicas:
"""

#  Negação (not):
"""
Fazendo a negação, se o valor booleano for veradeiro o resultado será falso 
se for falso o resultado será verdadeiro, ou seja, sempre ao contrário
"""

print(not ativo)

logado = False

#  Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

#  E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros 

True ande True -> True
True and False -> False
False and True -> False
False and False -> False
"""

