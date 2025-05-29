"""
🎮 Exercício: Loja de Jogos

🧩 Descrição:
Este sistema simula uma Loja de Jogos Online. A loja permite o cadastro de clientes,
cadastro de jogos, compra de jogos e exibição do histórico de compras para cada cliente.

🎯 Objetivo:
Implementar um sistema orientado a objetos com as seguintes funcionalidades:
- Cadastro de clientes (comum e premium)
- Cadastro de jogos
- Compra de jogos
- Histórico de compras por cliente

📚 Requisitos e Estrutura:

1. Classe Cliente (abstrata)
   Atributos:
     - nome
     - email
     - biblioteca (lista de jogos comprados)
   
   Métodos:
     - comprar_jogo(jogo)
     - exibir_biblioteca()
     - registrar_compra(jogo) (abstrato)

2. Subclasses ClienteComum e ClientePremium (herdam de Cliente)
   - ClienteComum:
       * paga o valor cheio do jogo
   - ClientePremium:
       * recebe 20% de desconto nas compras

3. Classe Jogo
   Atributos:
     - titulo
     - preco

4. Classe Historico
   Cada cliente possui um histórico de compras contendo:
     - Título do jogo
     - Data da compra
     - Preço pago
"""


from abc import ABC, abstractmethod
from datetime import datetime

class Cliente(ABC):
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self.biblioteca = []

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email
    
    def comprar_jogo(self, jogo):
        self.registrar_compra(jogo)
        print(f"{self.nome} comprou o jogo: {jogo.titulo}")

    def exibir_biblioteca(self):
        if not self.biblioteca:
            print("Biblioteca vazia.")
        else:
            print("Jogos na biblioteca:")
            for jogo in self.biblioteca:
                print(f"- {jogo.titulo}")

    @abstractmethod
    def registrar_compra(self, jogo):
        pass

class ClienteComum(Cliente):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.historico = [] # Cada cliente tem seu proprio historico

    def registrar_compra(self, jogo):
        valor_pago = jogo.preco # Cliente comum paga valor cheio

        # Registrar no historico
        registro = Historico(
            titulo = jogo.titulo,
            data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            valor_pago = valor_pago
        )

        self.historico.append(registro)

        self.biblioteca.append(jogo)

        print(f"\n {self.nome} comprou '{jogo.titulo}' por R${valor_pago:.2f}.")

    def comprar_jogo(self, jogo):
        self.registrar_compra(jogo)

    def exibir_historico(self):
        if not self.historico:
            print("Historico vazio até o momento...")
        else:
            for item in self.historico:
                print(f"{item}")



class ClientePremium(Cliente):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.historico = []

    def registrar_compra(self, jogo):
        valor_pago = jogo.preco * 0.80

        registro = Historico(
            titulo = jogo.titulo,
            data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            valor_pago = valor_pago
        )

        self.historico.append(registro)

        self.biblioteca.append(jogo)

        print(f"\n {self.nome} comprou '{jogo.titulo}' por R${valor_pago:.2f}.")
        
    def comprar_jogo(self, jogo):
        self.registrar_compra(jogo)

    def exibir_historico(self):
        if not self.historico:
            print("Historico vazio até o momento...")
        else:
            for item in self.historico:
                print(f"{item}")


class Jogo:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.preco = preco

class Historico:
    def __init__(self, titulo, data, valor_pago):
        self._titulo = titulo
        self._data = data
        self._valor_pago = valor_pago

    @property
    def titulo(self):
        return self._titulo 

    @property
    def data(self):
        return self._data 

    @property
    def valor_pago(self):
        return self._valor_pago 

    def __str__(self):
        return f"Titulo: {self.titulo} | Data: {self.data} | Valor pago: R${self.valor_pago:.2f}"
    


jogo1 = Jogo("Minecraft", 79.90)
jogo2 = Jogo("Fifa 25", 109.99)
jogador1 = ClienteComum("Rafael", "rafaelzampier14@gmail.com")
jogador2 = ClientePremium("Barbara", "barbarapimentel@gmail.com")

jogador1.comprar_jogo(jogo1)
jogador1.comprar_jogo(jogo2)
jogador1.exibir_biblioteca()
jogador1.exibir_historico()

jogador2.comprar_jogo(jogo2)
jogador2.exibir_biblioteca()
jogador2.exibir_historico()
    
   
