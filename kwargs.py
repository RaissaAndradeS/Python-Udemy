"""
**kwargs

Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mias um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionario.


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}') # pessoa.titel() para primeira maiuscula

cores_favoritas(Marcos='verde' , Julia='amarelo' , Fernanda='azul' , Vanessa='branco')


# Obs: Os parâmetros *args e **kwargs não são obrigatórios


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


# Nas nossas funções, podemos ter (nesta ordem):

# - Parâmetros obrigatórios;
# - *args;
# - Parâmetros default (não obrigatórios);
# - **kwargs;

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(**kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda por que é importante manter a ordem dos parâmetros na declaração

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# a = 1
# b = 2
# args = (3,)
# kwargs = {'sobrenome': 'University', 'cargo':'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Função com a ordem incorreta de parâmetros

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]
"""

# Desempacotar com **Kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nome(**nomes))


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3) TypeError

soma_multiplos_numeros(**dicionario, lang='Python')
