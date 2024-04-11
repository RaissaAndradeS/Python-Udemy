"""
Decorators com diferentes assinaturas



"""

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando

print(saudacao('Angelina'))


# A segunda função não vai funcionar porque ele espera receber so um parametro
# print(ordenar('Picanha', 'Batata Frita'))

# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern (*args, **kwargs)

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'



print(ordenar('Picanha', 'Batata Frita'))


# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada


@gritar
def lol():
    return 'lol'

print(lol())


# Obs: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))



# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorretor! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 15)) # 25
print(soma_dez(1, 10)) # Valor incorretor! Primeiro argumento precisa ser 10

print(comida_favorita('sushi', 'churrasco')) # Valor incorretor! Primeiro argumento precisa ser pizza
print(comida_favorita('pizza', 'churrasco')) # pizza e churrasco


