'''
Exercício: Sistema de Controle de Pets
Crie um sistema simples para gerenciar pets em um pet shop.

Requisitos:
Crie uma classe chamada Pet.

No construtor (__init__), defina os seguintes atributos:

nome

especie (Ex: cachorro, gato...)

idade

Crie os seguintes métodos:

apresentar: imprime uma frase com o nome, espécie e idade do pet.

fazer_aniversario: aumenta a idade do pet em 1 ano e imprime uma mensagem de parabéns.

Crie um destrutor (__del__) que imprima uma mensagem dizendo que o pet foi removido do sistema.
'''

class Pet:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def apresentação(self):
        print(f"Ola, eu sou o {self.nome}, sou um {self.especie} e tenho {self.idade} anos de idade.")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Feliz aniversario {self.nome}, agora você tem {self.idade} anos de idade")

    def __del__(self):
        print(f"Removendo o pet {self.nome} do sistema.")

pet1 = Pet("Rex", "Cachorro", 3)
pet1.apresentação()

pet1.fazer_aniversario()

del pet1