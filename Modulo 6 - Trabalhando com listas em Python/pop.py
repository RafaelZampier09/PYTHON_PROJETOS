linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens)
print(linguagens.pop())  # java
print(linguagens)
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
print(linguagens)

# No pop ele remove o ultimo valor que esta na lista, a não ser que seja passado um indice especifico para remoção