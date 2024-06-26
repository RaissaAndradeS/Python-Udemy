"""
POO - Herança Múltipla

Herança Múltipla é a possibilidade de uma classe herdar múltiplas classes, fazendo com que a
classe filha herde todos os atributos e métodos de todas as classes herdadas

# Obs: A herança múltipla pode ser feita de duas maneiras:
        - Por Multiderivação Direta;
        - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivaçãp Direta
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes

"""


class Animal:
    
    def __init__(self, nome):
        self.__nome = nome
        
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    

class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def nadar(self):
        return f'{self._Animal__nome} está nadando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    
    
class Terrestre:
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def andar(self):
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'
    

class Pinguim(Terrestre, Aquatico):  # Se alterar a ordem, muda o resultado
    
    def __init__(self, nome):
        super().__init__(nome)




baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

#tatu = Terrestre('Xim')
#print(tatu.andar())
#print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  #Method Resolution Order - MRO,   Eu sou Tux da terra!




# Objeto é instância de ...

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de Object? {isinstance(tux, object)}')
