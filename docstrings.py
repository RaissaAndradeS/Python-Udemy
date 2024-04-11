"""
Documentando funções com Docstrings

Obs: podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__

podemos ainda fazer acesso a documentação com a função help()
"""

print(help(print()))

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

print(diz_oi())

print(help(diz_oi()))

print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """"
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a potencia informada.
    :param numero: Numero que desejamos gerar o exponencial 
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """

    return numero ** potencia