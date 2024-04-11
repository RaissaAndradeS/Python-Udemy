"""
Leitura de Arquivos

Para ler um conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literamente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o caminho para o arquivo a ser lido. Essa
função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode = r -> Modo de leitura -> read()

"""

# Exemplo

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

# retorna uma string com o ret

ret = arquivo.read()

print(type(ret))

print(ret)

print(arquivo.read())

# OBS: O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# A função le todo conteúdo do arquivo



