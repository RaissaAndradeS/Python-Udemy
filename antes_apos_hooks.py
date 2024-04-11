"""
Unittest - Antes e após hooks


hooks - são os testes em si. Ou seja, a execução dos testes.


setup() -> é executado antes de cada método de teste. É util para criarmos instâncias de objetos ou outros dados;

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com
banco de dados.
"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do SetUp
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # Configurações do tearDown()
        pass