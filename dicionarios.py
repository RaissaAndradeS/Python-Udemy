"""
Dicionários

Obs: Em algumas linguagens de progrmação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs: Sobre dicionários
     - Chave e valor são separados por dois pontos 'chave : valor';
     - Tanto chave quanto valor podem ser de qualquer tipo de dado;
     - Podemos misturar tipos de dados;

"""

print(type({}))

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# obs: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('py'))
# print(paises.get('ru'))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
russia = paises.get('ru')

# Caso o get não encontre o objeto com a chave informada será retornado o valo None e não será gerado KeyError

if russia:
    print('Encontrei o país')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrãp para caso não encontremos o objeto com a chave informada

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não encontrado')

print(f'Encontrei o país {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Podemos verificar se determinada chave se encontra em um dicionário (eua: true, estados unidos: false)

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves de dicionários

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# forma 2
novo_dado = {'mai': 500}

receita.update(novo_dado) #receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão1: A dorma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão2: Em dicionários, Não podemos ter chaves repetidas

# Remover dados de um dicionário

# Forma 1 - Mais comum

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

ret = receita.pop('mar')
print(ret)

print(receita)

# Obs 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# Obs 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
# Obs: Neste caso o valor removido não é retornado

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos produtos.
"""
Carrinho de Compras
        Produto1: 
            - nome;
            - quantidade;
            - preço;
        Produto 2: 
            - nome;
            - quantidade;
            - preço;

  
"""
# 1 - Poderiamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar uma dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cada informação

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

#d.clear()

#print(d)

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() # Deep Copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionário

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmentros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave um valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)