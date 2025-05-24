class Estudante:
    escola = "DIO" # Atributo / Variavel da classe 

    def __init__(self, nome, matricula):
        self.nome = nome # Atributos do objeto
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante("Rafael Zampier", 123)
aluno_2 = Estudante("Barbara Pimentel", 456)
mostrar_valores(aluno_1, aluno_2)
Estudante.escola = "Python"

aluno_3 = Estudante("Jose Marcos", 578)
aluno_1.matricula = 789
mostrar_valores(aluno_1, aluno_2, aluno_3)

