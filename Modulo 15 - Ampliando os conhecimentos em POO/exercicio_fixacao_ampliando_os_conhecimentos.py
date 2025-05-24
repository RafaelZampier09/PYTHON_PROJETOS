'''
Exercício – Sistema de Funcionários
Crie uma estrutura para representar funcionários de uma empresa, seguindo as orientações abaixo:

Requisitos:
1. Classe Abstrata: Funcionario
Atributos de instância:

nome

salario_base

Atributo de classe:

empresa (igual para todos os funcionários, por exemplo: "Tech Solutions")

Método abstrato:

calcular_salario(): retorna o salário final (cada tipo de funcionário calcula de um jeito)

2. Subclasses Concretas:
FuncionarioCLT:

Salário final = salário base – desconto de 8% de INSS.

FuncionarioPJ:

Salário final = salário base sem desconto, mas sem benefícios.

3. Métodos de classe e estáticos
Em Funcionario:

@classmethod def mudar_empresa(cls, nova_empresa) – altera o nome da empresa para todos.

@staticmethod def validar_salario(valor) – retorna True se for positivo, False se for zero ou negativo.
'''


'''
| Conceito  / Para que serve    |                                                                   Onde aparece                       |
| ----------------------        | ------------------------------------                                                                 |
| Classe Abstrata - Não pode ser instanciada, serve apenas como molde                                   | `class Funcionario(ABC)`             |
| Método Abstrato - Sempre deve ser implementada nas classes filhas                                     | `@abstractmethod calcular_salario()` |
| Atributo de Classe - Atributo que pertence a classe e sempre sera compartilhada                       | `empresa = "DHL"`                    |
| Método de Classe - Recebe a classe como argumento e permite alterar o atributo da classe              | `@classmethod mudar_empresa()`       |
| Método Estático - Metodo que não precisa de self e nem cls, ainda não depende do objeto/classe        | `@staticmethod validar_salario()`    |
| Atributos de Instância - Deve ser declarado nas classes filhas da classe abstrada                     | `self.nome`, `self.salario_base`     |
| Polimorfismo - Permite que uma mesma interface tenha comportamentos diferentes em classes diferentes  | `calcular_salario()` nas subclasses  |

'''

from abc import ABC, abstractmethod

class Funcionario(ABC):
    empresa = "DHL"  # Atributo da classe, sempre sera compartilhado entre todos os funcionarios


    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    @classmethod # Pode altear o atributo da classe e recebe a classe como argumento
    def mudar_empresa(cls, empresa): # Permite alterar o nome da empresa
        Funcionario.empresa = empresa

    @staticmethod # Metodo que não precisa de self e nem CLS
    def validar_salario(salario_base):
        return salario_base > 0

    @abstractmethod   # Toda a classe que herda de funcionario deve obrigatoriamente implementar o metodo marcado com o valor de abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioCLT(Funcionario):
    def calcular_salario(self):
        return f"Salario = {self.salario_base * 0.92}\nBeneficio = Todos"
    
class FuncionarioPJ(Funcionario):
    def calcular_salario(self):
        return f"Salario = {self.salario_base}\nBeneficio = Nenhum"
    
clt = FuncionarioCLT("Rafael", 2000)
pj = FuncionarioPJ("Bruna", 5000)

print(clt.calcular_salario())
print(pj.calcular_salario())

Funcionario.mudar_empresa("Nova Tech")
print(Funcionario.empresa)

clt_2 = FuncionarioCLT("Barbara", -100)
print(clt_2.validar_salario(clt_2.salario_base))
        