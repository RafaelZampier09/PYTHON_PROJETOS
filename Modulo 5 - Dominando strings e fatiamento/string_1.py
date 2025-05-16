nome = "rafAel"

print(nome.upper()) # Deixa todas as letras em maiusculo.
print(nome.lower()) # Deixa todas as letras em minusculo.
print(nome.title()) # Deixa apenas a primeira letra em maiusculo, no caso de uma frase, deixa todas as primeiras letras de cada palavra desta forma.


texto = "  Ola Mundo!    "

print(texto + ".")
print(texto.strip() + ".") # Corta os espaços do texto.
print(texto.rstrip() + ".") # Corta os espaços do texto apenas na direita.
print(texto.lstrip() + ".") # Corta os espaços do texto apenas na esquerda.

menu = "Java"

print("####" + menu + "####")
print(menu.center(14)) # Ele ira definir o print com 14 caracteres, porém com a variavel menu centralizada.
print(menu.center(14, "#")) # Ele ira definir o print com 14 caracteres, porém com a variavel menu centralizada e com os outros caracteres sendo '#'.
print("Dados processados com sucesso".center(39, "="))
print("J-a-v-a")
print("-".join(menu)) # Faz com que cada letra fique separada com '-'.
