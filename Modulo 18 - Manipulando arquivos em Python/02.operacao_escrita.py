arquivo = open(r"C:\Users\rafae\OneDrive\Documentos\Curso_Dio\Modulo 18 - Manipulando arquivos em Python\teste.txt", "w") # Abre o arquivo em modo escrita
arquivo.write("Escrevendo dados em um novo arquivo.") # Coloca um texto dentro do arquivo
arquivo.writelines(["\n","Escrevendo", "um", "novo", "texto"]) # Adiciona um tipo iteravel dentro do arquivo
arquivo.close()
