
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# Mesma coisa que o sort, com a diferenã que ele é uma função e o sort é um metodo

lista =  [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lista)