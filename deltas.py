"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 15:03:24.57388
data_final = dd/mm/yyyy   28:34:23.9483297

delta = data_final - data-inical

"""

import datetime

# temos a data de hoje
data_hoje = datetime.datetime.now()

# data para começar o semestre da UnB
comeco = datetime.datetime(2024, 3, 18, 0)

tempo_para_comeco = comeco - data_hoje

print(type(tempo_para_comeco))

print(repr(tempo_para_comeco))

print(tempo_para_comeco)

print(tempo_para_comeco.days)

print(f'Faltam {tempo_para_comeco.days} dias, {tempo_para_comeco.seconds //60 // 60} horas...')


data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)

