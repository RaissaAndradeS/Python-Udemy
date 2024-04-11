"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Prevenindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.


A forma geral mais simples é:

try:
        //execução problemática
except:
        // o que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.


try:
    len(5)
except:
    print('Deu algum problema')

# Obs: tratar erro de forma genérica não é amelhor forma de tratamento de erros. O idela é sempre
# tratar de forma específica


# Exemplo - tratando um erro específico

try:
    geek()
except NameError:
    print(f'Você está tratando uma função inexistente')



"""

Erro que dará: TypeError, ai você vai no terminal e copia e coloca no lugar de NameError 


try:
    len(5)
except NameError:
    print(f'Você está tratando uma função inexistente')
    
    
try:
    len(5)
except NameError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
    
"""

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    # len(5)
    # geek()
    print('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print(f'Deu um erro diferente')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(7, "game"))  # dic e Geek vai dar certo