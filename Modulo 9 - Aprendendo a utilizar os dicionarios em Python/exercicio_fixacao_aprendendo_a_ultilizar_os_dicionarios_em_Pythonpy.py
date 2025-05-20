"""
Exercício: Cadastro de Alunos

Crie um programa que permita cadastrar informações de alunos e suas notas.

O programa deve:
1. Criar um dicionário chamado `alunos` onde:
   - A chave será o nome do aluno.
   - O valor será outro dicionário contendo:
     - "idade": idade do aluno
     - "nota": nota final do aluno

2. Permitir que o usuário cadastre pelo menos 3 alunos via input.

3. Após o cadastro:
   a) Exiba todos os alunos cadastrados com seus dados.
   b) Mostre a média das notas dos alunos.
   c) Permita buscar um aluno pelo nome e exibir seus dados.
   d) Use pelo menos 3 métodos da classe `dict`, como `.items()`, `.get()`, `.update()`, `.keys()` ou `.values()`.

(Extra) Tente remover um aluno pelo nome usando `.pop()`.

Dica: Use laços de repetição para organizar o fluxo de cadastro.
"""
ALUNOS_MINIMO = 3
alunos_cadastrados = 0
alunos = {}
media_notas = 0
soma_notas = 0
quantidades_alunos = 0

menu = """

Selecione a opção desejada

[1] Cadastrar novo aluno
[2] Exibir todos os alunos
[3] Buscar aluno especico
[4] Exibir média dos alunos
[5] Sair

"""

while True:
   opcao = int(input(menu))
   quantidade_cadastro = 0
   cadastro_informado = 1
   numero_aluno = 1


   if opcao == 1:
      quantidade_cadastro = int(input("Informe a quantidade de alunos que deseja cadastrar: "))
      if not quantidade_cadastro:
         print("Deve ter pelo menos um cadastro, tente novamente..")
      
      elif quantidade_cadastro <= 0:
          print("Opção invalida, tente novamente...")

      else:
         while quantidade_cadastro > 0:
            print(f"Cadastro numero {cadastro_informado}:")
            nome_aluno = input(f"Informe o nome do aluno {cadastro_informado}: ")
            idade_aluno = int(input(f"Informe a idade de {nome_aluno}: "))
            nota_aluno = float(input(f"Informe a nota de {nome_aluno}: "))
            alunos.update({nome_aluno : {"Idade":idade_aluno, "Nota":nota_aluno}})
            print(f"Aluno {nome_aluno} cadastrado com sucesso.")
            print("-"*30)

            cadastro_informado += 1
            quantidade_cadastro -= 1
         
         input("Pressione enter para voltar ao menu...")

   elif opcao == 2:
      for aluno, dados in alunos.items():
         print(f"Nome do aluno numero {numero_aluno}: {aluno}")
         for chave, valor in dados.items():
            print(f"{chave}:{valor}")
         print("-"*30)
         numero_aluno+=1
      input("Pressione enter para voltar ao menu...")

   elif opcao == 3:
      nome_aluno_buscado = input("Digite o nome do aluno que deseja ver: ")
      print("-"*30)
      print(f"Informações sobre {nome_aluno_buscado}: ")
      resultado_aluno_buscado = alunos.get(nome_aluno_buscado)
      if resultado_aluno_buscado is not None:
         for chave, valor in resultado_aluno_buscado.items():
            print(f"{chave}:{valor}")
      else:
         print(f"Não temos o aluno(a) {nome_aluno_buscado} em nosso banco de dados...")
      
   elif opcao == 4:
      print("-"*30)
      for dados in alunos.values():
         soma_notas += dados["Nota"]
         quantidades_alunos += 1
      media_notas = soma_notas/quantidades_alunos
      print(f"A media de notas até o momento é de: {media_notas:.2f}")
      input("Pressione enter para voltar ao menu...")
      
   elif opcao == 5:
       print("Obrigado por usar nosso sistema :)")
       break
      
   
   else:
       print("Opção invalida, tente novamente")