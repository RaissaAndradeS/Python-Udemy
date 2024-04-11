"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência", "dados"

# Separador por onto e vírgula

1; 2; 3; 4; 5; 6;

"geek"; "university"; "python"; "ciência"; "dados"

# Separadoe por espço

1 2 3 4 5 6

"geek" "university" "python" "ciência" "dados"


http://dados.gov.br/dataget

# Possivel de se trabalhar mas não é ideal

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - Reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

"""
# Reader

from csv import reader


with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')



# DictReader

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")



# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")