# Filtro versão 1
'''
Nesse caso foram criadas 2 listas, e uma dessas listas será para armazenar os numeros pares da primeira lista
'''

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


# Filtro versão 2
'''
Fazendo o mesmo processo acima mas com list comprehension
'''

numeros2 = [1, 30, 21, 2, 9, 65, 34]
pares2 = [numero for numero in numeros2 if numero % 2 == 0]
print(numeros2)
print(pares2)

# O primeiro numero é o retorno, ou seja, o que irá compor minha lista
# A segunda parte é a iteração, como se fosse o for na primeira versão
# A terceira parte é o if, para adicionar somente se uma condição for verdadeira, no caso do exemplo, é se for numero par


# Modificando a versão 1
'''
Neste caso vamos pegar a lista 1 e fazer todos os valores elevados ao quadrado
'''

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)


# Modificando a versão 2
'''
Neste caso vamos pegar a lista 1 e fazer todos os valores elevados ao quadrado mas com list comprehension
'''

quadrado2 = [numero ** 2 for numero in numeros2]
print(quadrado2)
print(quadrado)