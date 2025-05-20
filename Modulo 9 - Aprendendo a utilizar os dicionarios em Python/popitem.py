contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}


print(contatos)
contatos.popitem()
print("")
print(contatos)

# O popitem é parecido com o pop, mas ele remove o ultimo valor, no caso removeu o ultimo e-mail do dicionario