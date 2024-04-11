"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Iterar sobre dicionário


for chave in receita:   # Imprimindo receita
    print(chave)

for chave in receita:   # Imprimindo valores
    print(receita[chave])


for chave in receita:
    print(f' Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita)

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

print(receita)

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
    

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
