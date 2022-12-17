from functools import reduce

numeros = [1, 2, 6, 8, 6, 9, 2, 5, 7, 4]


def impar(x):
    if x % 2 == 1:
        return True

    return False


def suma(a, b):
    return a + b


resultado = filter(impar, numeros)
suma = reduce(suma, numeros)

print(list(resultado))
print(suma)