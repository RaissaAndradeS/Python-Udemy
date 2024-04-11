"""
Sistema de Arquivos - Manipulação


"""
import os

# Descobrindo se um arquivo ou diretório existe
# Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

# Diretório
# Paths relativos
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('outro')) # False

# Paths Absolutos é da raiz c://


# Criando arquivos

# Forma 1
open('arquivo-texte.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


"""
# Forma mais 'correta'

import os

os.mknod('arquivo-texte4.txt')

os.mknod('/home/geek/university.txt')


# OBS: Se vocÊ estiver utilizando no Mac Os, pode haver um erro de PermissionError
# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError 
"""

#  Criando diretórios

# os.mkdir('templetes')

# Obs: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError
# Obs: Se não tiver permissão para criar o diretório, dará um PermissionError


# Criando multi-diretórios(árvore de diretórios)

# os.makedirs('templates/geek/university')

os.makedirs('templates2/novo2/outro2', exist_ok=True)


# Renomear arquivos e diretórios

# diretórios

# os.rename('templates2/novo2', 'geek2')

# Obs: Se o diretório não existir, teremos um FileNotFoundError
# Obs: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos

# os.rename('geek2/outro2/teste.txt', 'geek2/outro2/geek.txt')

# os.rename('frutas.txt', 'cesta.txt')



# ATENÇÃO! Tome cuidado com os comandos de deleção, ao deletarmos um arquivo ou diretório, eles somem, não tem lixeira

# Removendo arquivos

# os.remove('geek.txt')

# Obs: Se vocês estiver no windows e o arquivo que você for deletar estiver em uso, você terá um erro

# Obs: Caso o arquivo não exista, teremos o FileNotFoundError

# Obs: Se vocÊ informar um diretório ao invés de um arquivo, teremos um IsADirectoryError


# Removendo diretórios vazios

# os.rmdir('templates')

# Obs: Se o diretório tiver qualquer conteúdo teremos um OSErros

# Obs: Se o diretório não existir, teremos um FileNotFoundError

"""
# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

"""

# Podemos remover uma árvore de diretórios vazios

# os.removedirs('geek2')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para


# Se quiser mandar o arquivo ou diretórios para lixeira, instalar o send2trash

# send2trash('') # Vai para lixeira e pode ser restaurado

# Obs: Se o arquivo não existir, teremos OSError


# Trabalhando com arquivos e diretórios temporarios
"""
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
"""
# Estamos criando um diretório temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro do bloco with


# Criando um arquivo temporário

import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University')
    tmp.seek(0)
    print(tmp.read())


# Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos 'b'



# Sem bloco with


arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()





arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

input()

arquivo.close()


