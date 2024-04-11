"""
Sistema de Arquivo e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importat
e fazer uso do módulo os

os -> Operating System - Sistema Operacional

"""

# Fazer o import
import os
import sys

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())


# Podemos checar se um diretório é absoluto ou relativo
# Obs: No windows, tomar cuidado pq a \ pode ser usado para programação e é separadores no windows

print(os.path.isabs('C:\\Users'))  #True


# Podemos identificar o sistema operacional com o módulo os
print(os.name) # nt / posix(linux e Max)

# No windows não da pra saber mais detalhes com o comando print(os.uname())

print(sys.platform)

print(os.getcwd())

# os.path.join(os.getcwd(), 'geek', 'university')

# print(os.getcwd())

# os.path.join() recebe dois parâmetros, sendo o primeiro diretório atual e o segundo o diretório que será juntado


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())

# mais detalhes

# print(os.scandir())

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos[0].inode())
# print(arquivos[0].is_dir()) é um diretório? False
# print(arquivos[0].is_file()) é um arquivo? true
# print(arquivos[0].is_symlink()) link simbolico? false
# print(arquivos[0].name) nome do arquivo
# print(arquivos[0].path) caminho até o arquivo
# print(arquivos[0].stat())  estatisticas

# Obs: quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo

# scanner.close()

