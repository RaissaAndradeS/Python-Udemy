"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples --> 'Raissa'
- Aspas duplas--> "Raissa"
- Aspas simples triplas--> '''Raissa'''
- Aspas duplas triplas--> """"""  

"""


#  Entrada de dados
#  print("Qual seu nome ?")
#  nome = input()  # Input-> Entrada

nome = input('Qual seu nome? ')

#  print("Qual sua idade ?")
#  idade = input()

idade = input('Qual sua idade?')

#  Exemplo de print 'antigo' 2.x
#  Processamento de dados
#  print('Seja bem-vindo(a) %s' % nome)


#  Exemplo de print 'antigo' 2.x
# Saída
#  print("A %s tem %s anos" % nome, idade)

#  Exemplo de print mais moderno 3.x

#  print("Seja bem-vindo(a) {0}".format((nome)))

#  print("A {0} tem {1} anos".format(nome, idade))

#  Mais moderno

print(f'Seja bem-vindo(a) {nome}')

print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2023 - int(idade)}')

"""
int(idade)=> cast 
Cast é a 'conversão' de um tipo de dado para outro.
"""