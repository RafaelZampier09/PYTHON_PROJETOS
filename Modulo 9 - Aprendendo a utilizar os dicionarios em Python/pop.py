contatos = {
    "rafaelzampier14@gmail":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

print(contatos.pop("josesilva@gmail.com"))
print(contatos)
contatos.pop("josesilva@gmail.com", {"Não encontrou"})


# No pop, ele remove um valor do dicionario, caso ele não exista, podemos colocar o {} como padrão