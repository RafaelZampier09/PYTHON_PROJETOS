contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

copia = contatos.copy()
copia["rafaelzampier14@gmail.com"] = {"nome": "Rafa"}

print(contatos["rafaelzampier14@gmail.com"])
print(copia["rafaelzampier14@gmail.com"])