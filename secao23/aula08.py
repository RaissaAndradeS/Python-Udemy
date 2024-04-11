import math


def circuferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circuferencia(8))


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


# cabecalho(texto=43, alinhamento='geek')  Errada, str e bool

