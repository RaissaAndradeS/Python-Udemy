"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
  - São reconhecidas, ou seja, seu escoó compreende, todo o programa

2 - Variáveis locais;
  - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.


 Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuímos o valor à mesma.

Exemplo em C:
int numero = 42

Exemplo em Java
int numero = 42

"""

numero = 42   # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)


numero = 2
# nome = 0
if numero > 10:
    novo = numero + 10  # A variavel 'novo' está declarada localmente dentro do bloco do if, portanto é local
    print(novo)

