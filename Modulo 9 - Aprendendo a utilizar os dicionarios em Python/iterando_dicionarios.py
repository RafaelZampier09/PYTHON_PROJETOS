contatos = {
    "rafaelzampier14@gmail":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

for chave, dados in contatos.items():
    print(chave, contatos[chave])
    for item in contatos[chave]:
        print(item)