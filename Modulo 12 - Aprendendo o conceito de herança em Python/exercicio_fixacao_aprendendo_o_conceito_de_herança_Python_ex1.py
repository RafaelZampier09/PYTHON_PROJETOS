'''
Exercício 1 – Herança Simples
Crie uma hierarquia de classes para um sistema escolar.

Requisitos:
Crie uma classe Pessoa com:

Atributos: nome, idade

Método: apresentar(), que imprime uma apresentação com o nome e idade.

Crie uma classe Aluno que herda de Pessoa e adicione:

Atributo: matricula

Método: estudar(), que imprime que o aluno está estudando.

Crie uma instância de Aluno e:

Chame o método apresentar()

Chame o método estudar()
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos de idade")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print("Estou estudando...")

aluno_1 = Aluno("Rafael", 22, 12345)
aluno_1.apresentar()
aluno_1.estudar()
