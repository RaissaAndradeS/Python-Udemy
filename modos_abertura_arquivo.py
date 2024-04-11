"""
Modos de Abertura de Arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo
+ -> Abre para o modo de atualização: Leitura e Escrita (Temos o controle do cursor)

# Obs: Abrindo o modo 'a' -> append, se o arquivo não existir será criado, Caso exista, o novo conteúdo
será adicionado ao final SEMPRE. Com o modo 'a', não controlamos o cursor



try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe')



with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(12)
    arquivo.write('Mais uma linha.\n')


