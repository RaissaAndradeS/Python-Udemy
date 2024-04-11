"""
int, str, float, List, Set, Dict, etc
"""


def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro('Geek')) # Mypy avisa


"""
- Literal type
- Union 
- Final 
- Typed dictionaries 
- Protocols 

"""

# Literal type


from typing import Literal


def pegar_status(usuario:str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1} + {num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1} + {num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
# calcula_v1('*' 3, 5) # não funciona pq não tem *


# com Literal

def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1} + {num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1} + {num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5) # erro


# Union

from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado




# Final


from typing import Final

NOME: Final = 'Geek'

print(NOME)

NOME = 'University'

print(NOME)

# NORMAL DA OK, MAS COM MYPY DA ERRO


from typing import final
# decorador


@final
class Pessoa:
    pass


class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estou estudando e estagiando...')


# Mypy não deveria herdar pessoa pq pessoal é final, teria que tirar 'Pessoa' de estudante


# Typed Dictionaries

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao ='3.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='vai', coisa=True)

print(outro)


# Protocols

from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


v1 = Venda()
#c1 = Curso()  
#c1.titulo = 'Programação em Python'


#estudar(c1)
estudar(v1)


# ADD O OBJ TITULO ABAIXO DE DE VENDA


