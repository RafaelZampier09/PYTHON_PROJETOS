"""
Exercício de Fixação – Strings em Python

Objetivo: Praticar os seguintes conceitos:
- Métodos úteis da classe string
- Interpolação de variáveis (f-strings)
- Fatiamento de strings
- String de múltiplas linhas

Instruções:
1. Solicite ao usuário:
   - Nome completo
   - Ano de nascimento
   - Curso atual
   - Uma frase favorita

2. A partir desses dados, exiba:
   a) O nome:
      - Em letras maiúsculas
      - Em letras minúsculas
      - Com a primeira letra de cada palavra em maiúscula

   b) Interpolação de variáveis:
      - Calcule a idade com base no ano atual
      - Exiba uma frase usando f-string:
        Exemplo: "Maria, você tem aproximadamente 26 anos e está matriculado no curso de Ciência de Dados."

   c) Fatiamento de strings:
      - Mostre os 3 primeiros e os 3 últimos caracteres do nome
      - Mostre a frase favorita invertida

   d) String de múltiplas linhas:
      - Exiba um resumo final com todos os dados formatado usando aspas triplas
"""

# Solitando ao usuario

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
curso_atual = str(input("Digite seu curso atual: "))
frase_favorita = str(input("Digite sua frase favorita: "))

# Exibindo o nome

print("Dados processados com sucesso".center(39, "="))
print("")
print(f"Nome em maiusculo: {nome.upper()}")
print(f"Nome em minusculo: {nome.lower()}")
print(f"Nome formatado: {nome.title()}")

# Interpolação de variaveis

print("")
idade = 2025 - ano_nascimento
print(f"{nome}, você tem aproximadamente {idade} anos e esta matriculado no curso de {curso_atual}.")

# Fatiamento de strings
print("")
print(f"Primeiros 3 caracteres do nome: {nome[:3].lower()}")
print(f"Ultimos 3 caracteres do nome: {nome[-3::].lower()}")
print(f"Frase invertida: {frase_favorita[::-1]}")

# Resumo
print("")
print(f"""
    RESUMO
Nome: {nome}
Curso: {curso_atual}
Idade: {idade}
Frase favorita: {frase_favorita}
""")