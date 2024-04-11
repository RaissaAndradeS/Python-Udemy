"""
Escrevendo um iterador customizado



class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def__iter__(self):
        return self

    def__next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1, 6)


it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


ou

for n in Contador (1, 61):
    print(n)

for n in range(1, 61):
    print(n)
"""