"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: o contrário não é verdadeiro. Ou seja, nem todo iterador é um generator.

    Outras informações:
        - Generators podem ser criados com funções geradoras;
        - Funções geradoras utilizam a palavra reservada yield;
        - Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

------------------------------------------------------------------
| - Funções                     | - Generator Funcions            |
------------------------------------------------------------------
| - Utilizam return             | - Utilizam yield                |
------------------------------------------------------------------
| - Retorna uma vez             | - Podem utilizar yield mútiplas |
------------------------------------------------------------------
| - Retorna um valor, exec      | - Retorna um generator, exec    |
------------------------------------------------------------------



gen = conta_ate(10)

for num in gen:
    print(num)


print(next(gen)) # 1

print('geek')

for num in gen:  # começa no 2
    print(num)
"""

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# Obs: Uma Generator Function não é um Generator, ela gera um generator

gen = conta_ate(5)

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



gen = list(conta_ate(10))

print(gen)


