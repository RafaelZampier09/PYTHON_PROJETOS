'''
Exercício: Classe Produto com Encapsulamento e Propriedades
Crie uma classe chamada Produto com os seguintes atributos:

nome (público)

_preco (protegido — com underline)

_estoque (protegido — com underline)

Regras:
Use @property para permitir acesso ao preco e ao estoque.

Use @setter:

Para preco: não permitir definir valores negativos (exiba uma mensagem de erro).

Para estoque: também não permitir valores negativos.

Crie um método chamado vender que:

Recebe a quantidade desejada.

Reduz o estoque, caso tenha quantidade suficiente.

Caso não tenha estoque suficiente, exibe mensagem de erro.

Crie um método chamado repor para aumentar o estoque.
'''

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def preco(self):
        return self._preco
    
    @property
    def estoque(self):
        return self._estoque
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            print("Favor colocar um valor acima de 0...")
        else:
            self._preco = valor

    @estoque.setter
    def estoque(self, quantidade):
        if quantidade <= 0:
            print("Favor colocar umma quantidade acima de 0...")
        else:
            self._estoque = quantidade

    def vender (self, quantidade_desejada):
        if quantidade_desejada > self._estoque:
            print("Não temos o estoque disponivel para esse total de venda...")
        elif quantidade_desejada <= 0:
            print("Favor digitar uma quantida valida...")
        else:
            self._estoque -= quantidade_desejada
            print(f"Venda de {quantidade_desejada} produtos realizada com sucesso!")

    def reposicao (self, quantidade_reposta):
        if quantidade_reposta <= 0:
            print("Favor repor uma quantidade maior que 0...")
        else:
            self._estoque += quantidade_reposta

produto1 = Produto("Caneta", 2.50, 200)

print(produto1.preco)
produto1.preco = -4
produto1.reposicao(20)
produto1.vender(50)
produto1.vender(200)