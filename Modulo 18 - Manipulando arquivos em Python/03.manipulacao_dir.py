import os
import shutil
from pathlib import Path # Sempre importar essa biblioteca para trabalhar caminhos e diretorios em python

ROOT_PATH = Path(__file__).parent # File é uma variavel especial que contem o caminho completo do codigo atual e o path cria um objeto para esse caminho
# print(ROOT_PATH.parent) # Aqui sempre ira pegar o arquivo que esta cima, no caso, a pasta do arquivo em execução

# os.mkdir(ROOT_PATH / "novo-diretorio") # a / nesse caso, pode ser interpretado em qualquer sistema operacional
# mkdir cria um unico diretorio no local especifico

# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close() # Criando um arquivo em modo de escrita

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-arquivo.txt") # Alterando o nome de um arquivo

# os.remove(ROOT_PATH / "novo-arquivo.txt") # Removendo um arquivo

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") # Movendo um arquivo de diretorio