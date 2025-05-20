contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

contatos.update({"rafaelzampier14@gmail.com" : {"Nome": "Rafa"}}) # Nesse caso, ele pegou o email e ira deixar somente com o outro dicionario com o nome, retirando as outras informações
print(contatos)

contatos.update({"bs527638@gmail.com" : {"Nome":"Barbara", "Sobrenome":"Pimentel"}}) # Nesse caso, ele pegou o email e ira deixar somente com o outro dicionario com o nome, retirando as outras informações
print(contatos)

# No caso do update, ele ira pegar a chave de referência e deixa somente com os valores passado, caso não exista, irá adicionar