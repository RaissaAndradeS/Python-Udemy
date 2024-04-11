"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

# python -m doctest -v doctests.py


def soma(a, b):
   aspas #soma os números a e b

    # >>> soma(1, 2)
     3
     # aspas
    return a + b

print(soma(3, 4)) #7




# Outro exemplo, aplicando o tdd


def duplicar(valores):
    #duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 3, 4, 8]

    #>>>duplicar([])
    []

    #>>>duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>>duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    return [2 * elemento for elemento in valores]


# Erro inesperado
# aspas simples pq ja tem aspas duplas

def fala_oi():
    #Falaoi
    #>>>fala_oi()
    'oi'
    #
    return "oi"


"""


def verdade():
    """Retorna verdade

    >>>verdade()
    True
    """
    return True


