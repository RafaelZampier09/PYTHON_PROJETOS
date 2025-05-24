from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligar TV")

    def desligar(self):
        print("Desligar TV")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    
    def ligar(self):
        print("Ligar TV")

    def desligar(self):
        print("Desligar TV")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()