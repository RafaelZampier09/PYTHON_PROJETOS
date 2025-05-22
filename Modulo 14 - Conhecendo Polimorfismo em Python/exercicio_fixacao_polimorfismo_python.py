'''
🧠 Exercício: Animais Falantes
Crie um programa com uma classe base chamada Animal, e três classes derivadas: Cachorro, Gato e Pato.
Cada uma deve ter um método falar() que imprime o som que o animal faz.

Depois, crie uma função chamada faz_barulho() que recebe um objeto do tipo Animal e chama o método falar().

✅ Requisitos:
A classe base Animal deve ter o método falar() (pode ser vazio ou com pass).

As classes Cachorro, Gato e Pato devem sobrescrever o método falar() com sons diferentes.

A função faz_barulho() deve aceitar qualquer objeto que seja uma instância de Animal (ou herde dela).

Teste a função passando diferentes animais.


'''

class Animal:
    def falar(self):
        print("Animal falando...")

class Cachorro(Animal):
    def falar(self):
        print("Auau!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

class Pato(Animal):
    def falar(self):
        print("Quack!")

def faz_barulho(animal):
    animal.falar()

faz_barulho(Cachorro())
faz_barulho(Gato())
faz_barulho(Pato())

