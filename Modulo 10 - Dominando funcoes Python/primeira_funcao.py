def exibir_mensagem(): # Aqui é declarado uma função base, sem argumento ou seja, ela ira executar sem a necessidade de parametro
    print("Ola mundo!")

def exibir_mensagem_2(nome): # Aqui declaramos uma função com o argumento nome sendo necessario, caso não ocorra a passagem deste argumento, sera errado
    print(f"Seja bem vindo(a) {nome}")

def exibir_mensagem_3(nome="Anônimo"): # Aqui declaramos uma função com o argumento nome sendo necessario, porém quando não passamos, temos um default sendo o nome de "Anonimo"
    print(f"Seja bem vindo(a) {nome}")


exibir_mensagem()

exibir_mensagem_2("Rafael")

exibir_mensagem_3()