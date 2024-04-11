"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
"""

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora corente
print(datetime.datetime.now())  # 2024-03-15 20:32:14.773657


# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))  # datetime.datetime(2024, 3, 15, 20, 33, 40, 177171)


# Replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)


# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo

inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)


evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

# Recebendo dados do usuário e convertendo para data

print(type('31/12/2018'))

print(evento)


nascimento = input('Informe sua data de nascimento (dd/mm/yyy): ')

nascimento = nascimento.split('/')


nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))


# Acesso individual dos elementos de data e hora


evento = datetime.datetime.now()

print(evento.year)  # Ano
print(evento.month) # Mês
print(evento.day)  # Dia
print(evento.hour)  # Hora
print(evento.minute)  # Minuto
print(evento.second)  # Segundo
print(evento.microsecond)  # Microsegundo




