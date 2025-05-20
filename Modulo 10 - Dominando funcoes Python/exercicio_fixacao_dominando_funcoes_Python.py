"""
Exercício: Sistema de Notas com Funções
Crie um programa com as seguintes funções:

1. cadastrar_aluno(nome, nota)
Deve receber o nome de um aluno e sua nota.

Retorna um dicionário com os dados: {"nome": ..., "nota": ...}

2. calcular_media(lista_notas)
Recebe uma lista de notas e retorna a média delas.

3. exibir_alunos(lista_alunos)
Recebe uma lista de alunos (cada um é um dicionário) e imprime seus dados formatados.

4. (Opcional) buscar_aluno(lista_alunos, nome)
Procura um aluno pelo nome e exibe sua nota, ou informa que ele não foi encontrado.
"""

# Ira executar o cadastro do aluno, recebendo dois paramatros
def cadastrar_aluno(nome, nota):
    return{"nome": nome, "nota": nota}


#Ira calcular a media a partir da lista de notas, essa criada posteriormente as funcções
def calcular_media(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas)/len(lista_notas)

# Ira exibir os alunos conforme a lista de alunos (criada posteriormente) em que sera mostrado o nome e a nota
def exibir_alunos(lista_alunos):
    print("\n Lista de Alunos Cadastrados: ")
    for aluno in lista_alunos:
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")

# Ira exibir o aluno procurado, que sera buscado na lista de alunos a partir do nome
def buscar_aluno(lista_alunos, nome):
    for aluno in lista_alunos:
        if aluno['nome'].lower() == nome.lower():
            print(f"\n Aluno encontrado: {aluno['nome']} | Nota: {aluno['nota']}")
            return
    print("\nAluno não encontrado")


# Lista vazia de alunos
alunos = []

# Cadastro de pelo menos 3 alunos, que serão direcionados a lista (alunos)
print("Cadastro de alunos")
for i in range(3):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    nota = float(input(f"Informe a nota de {nome}: "))
    aluno = cadastrar_aluno(nome, nota)
    alunos.append(aluno)

# Executa a função exibir alunos a partir da lista de alunos
exibir_alunos(alunos)


# Cria uma lista de notas, onde pega o valor de 'nota' na lista de alunos
notas = [aluno['nota'] for aluno in alunos]
media = calcular_media(notas)
print(f"Media dos alunos: {media:.2f}")

# Busca o nome de um aluno que esta na lista (alunos)
nome_busca = input("\nDigite o nome de um aluno para buscar: ")
buscar_aluno(alunos, nome_busca)
    