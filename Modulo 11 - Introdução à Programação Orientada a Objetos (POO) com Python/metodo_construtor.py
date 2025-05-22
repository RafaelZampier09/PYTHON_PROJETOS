"""
Metodo construtor

O metodo construtor sempre é executado quando uma nova
instância da classe é criada. Nesse método inicializamos
o estado do nosso objeto. Para declarar o método construtor
da classe, criamos um método com o nome __init__
"""

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado