contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

contatos["rafaelzampier14@gmail.com"].setdefault("Nome","Guilherme") # Nesse caso não irá alterar, pois no existe nome na chave do e-mail
print(contatos)

contatos["rafaelzampier14@gmail.com"].setdefault("Cidade", "Osasco") # Nesse caso irá adicionar a chave cidade no e-mail com o valor de Osasco
print("")
print(contatos)

contatos.setdefault("Nome","Rafael")

# No caso do set default, caso exista a chave, ele não irá alterar o valor, caso não exista, ele ira adicionar com aquele valor informado