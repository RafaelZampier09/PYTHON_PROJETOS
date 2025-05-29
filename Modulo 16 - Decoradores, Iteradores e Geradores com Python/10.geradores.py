def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 3, 5]):
    print(i)

