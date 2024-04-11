def multiplicar (num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)

print(f'O resultado é {resultado}')

print(f'O resultado é {multiplicar(9, 4):.2f}')

print(f'{(media := 8 / 2)} pe a metade de {media * 2}')



"""
geek: str = 'Geek University'


print(f"geek='{geek}'")

"""
# mesmo resultado mais simplificado
geek: str = 'Geek University'


print(f'{geek}')


print(f'{geek.upper()[::-1]=}')

