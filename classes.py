"""
POO - Classes

Em POO, Classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa

    Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
    iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer represenrar no nosso sistema é o de ligar e desligar.


Em Python, para definir uma classe utilizimaos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado

OBS: Quando nomeamos NOSSAS classes em Python, utilizamos por converção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as uniciais de ambas as palabras em maiúsculo, todas juntas.

    Dica Geek: Em computação não utilizamos:
        - Acentuação;
        - Caracteres especiais
        - Espaços ou similiares para nomes de classes, atributos, métodos, arquivos, diretórios e etc


OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade. (nesses exemplos: Lampada, ContaCorrente, Produto,
Usuario).

"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()

print(type(lamp))


# int é uma classe interna do python e por isso que é minúscula



