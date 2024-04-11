"""
Módulo Collections - Default Dict

"""
# Recap Dicionário

dicionario = { 'curso': 'Porogramação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

# print(dicionario['outro']) KeyError

# Default dict  -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
# podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
# um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
# e o valor default será atribuido

# Obs: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

# print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não

print(dicionario)