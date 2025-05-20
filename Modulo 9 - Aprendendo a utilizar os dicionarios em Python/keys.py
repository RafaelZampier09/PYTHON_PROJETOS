contatos = {
    "rafaelzampier14@gmail":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

resultado = contatos.keys()
print(resultado)

resultado = contatos["rafaelzampier14@gmail"].keys()
print(resultado)

# No Keys ele retorna somente as chaves do dicionadio, no caso do nosso exemplo, temos os dois e-mails