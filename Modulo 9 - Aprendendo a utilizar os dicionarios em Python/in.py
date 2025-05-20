contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

resultado = "rafaelzampier14@gmail.com" in contatos
print(resultado)

resultado = "barbarapimentel@gmail.com" in contatos
print(resultado)

# O in assim como de outras formas, verifica se o conteudo proposto esta contido em algo, no caso se a chave esta contida no dicionario