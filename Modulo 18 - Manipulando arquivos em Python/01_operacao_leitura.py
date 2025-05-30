arquivo = open(r"C:\Users\rafae\OneDrive\Documentos\Curso_Dio\Modulo 18 - Manipulando arquivos em Python\lorem.txt", "r") # Abre o arquivo em modo leitura

# print(arquivo.read())
# for linha in arquivo.readline(): # Traz uma letra por vez da primeira linha
#     print(linha)

# for linha in arquivo.readlines(): # Traz uma linha por vez do texto
#     print(linha)

while len(linha := arquivo.readline()): # := é um atribuidor de expressão que permite atribuir e usar uma variavel dentro da propria expresão do while
    print(linha)

arquivo.close() # Fecha o arquivo
