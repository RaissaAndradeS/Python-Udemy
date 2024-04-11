"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidade individuais de código fonte.

Unidades individuais podem ser:
    - funções,
    - métodos,
    - classes,
    - módulos,
    - etc

# Obs: Teste unitário não é específico da linguagem Python

Para criar nossos testes, criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos os 'assertions' no módulo.

Para rodar os testes. utilizamos unittest.main()


TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIfNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIn(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsInstance(a, b)      a é instância de b
assertNotIsInstance(a, b)   a não é instância de b


Por convenção, todos os testes de um test case, devem ter seu nome
iniciado com test_

Para executar os testes com unittest

python nome_do_arquivo.py

Outra forma de executar os testes com unittest no modo verbose

python nome_dp_modulo -v


Docstrings nos testes
Podemos acrescentar (e é recomendado) docstring nos nossos testes.

"""

# Prática - a abordagem TDD