"""
📌 Gerenciador de Tarefas Diárias

Este script implementa um gerenciador simples de tarefas utilizando arquivos em Python.
O programa permite ao usuário registrar, listar, buscar e excluir tarefas salvas em um arquivo de texto.

🔧 Funcionalidades:
1. Adicionar nova tarefa (salva no arquivo "tarefas.txt").
2. Listar todas as tarefas existentes.
3. Buscar tarefas por palavra-chave.
4. Excluir todas as tarefas com confirmação do usuário.
5. Utiliza 'with' para manipulação segura de arquivos.
6. Utiliza 'Path' do módulo pathlib para lidar com caminhos de forma robusta.
7. Verifica se o arquivo já existe antes de tentar acessá-lo.

💡 Cada tarefa é registrada em uma nova linha no arquivo e pode conter apenas a descrição,
ou opcionalmente incluir data e hora da criação para maior controle.
"""

from pathlib import Path
from datetime import datetime

ROOT_PATH = Path(__file__).parent

def menu():
    print("""
    ---------- MENU ----------
    [1] ADICIONAR TAREFA
    [2] LISTAR TAREFAS
    [3] BUSCAR TAREFA
    [4] CONCLUIR TAREFA
    [5] EXCLUIR TODAS TAREFAS
    [0] SAIR
""")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção invalida, digite apenas numeros.")
        return -1
    
def proximo_id_tarefa():
    caminho = ROOT_PATH / "tarefas.txt"

    if not caminho.exists():
        return 1
    
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            return 1
        ultima_linha = linhas[-1]
        try:
            id_str = ultima_linha.split("|")[0].replace("Tarefa de numero ", "").strip()
            return int(id_str) + 1
        except:
            return 1
        
def nova_tarefa():
    id_tarefa = proximo_id_tarefa()
    while True:
        try:
            tarefa = input("Digite uma nova tarefa: ")
            data_atual = datetime.now().strftime("%d/%m/%Y")
            hora_atual = datetime.now().strftime("%H:%M:%S")
            with open(ROOT_PATH / "tarefas.txt", "a", newline="", encoding="utf-8") as arquivo:
                arquivo.write(f"Tarefa de numero {id_tarefa} | Nome: {tarefa} | Horário/data de registro: {data_atual} às {hora_atual}\n")
            print("Tarefa registrada com sucesso.")
            return
        except Exception as exc:
            print(f"Entrada invalida, tente novamente, {exc}")

def listar_tarefas():
    try:
        with open(ROOT_PATH / "tarefas.txt", "r", newline="", encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
            if not linhas:
                print("Nenhuma tarefa registrada até o momento.")
                return
            for linha in linhas:
                partes = linha.strip().split("|")
                id_str = partes[0].replace("Tarefa de numero ","").strip()
                tarefa_str = partes[1].replace("Nome: ","").strip()
                horario_str = partes[2].replace("Horário/data de registro: ", "").strip()
                print(f"Tarefa de numero {id_str}:\nNome: {tarefa_str} | Data e horario de registro: {horario_str}")
                # print(linha)
                print("-"*80)
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler tarefas: {e}")

def buscar_tarefa():
    caminho = ROOT_PATH / "tarefas.txt"

    if not caminho.exists():
        print("Não temos nenhuma tarefa até o momento.")
        return
    
    while True:
        try:
            id = int(input("Digite o numero da tarefa que deseja buscar: "))
            with open(ROOT_PATH / "tarefas.txt", "r", newline="", encoding="utf-8") as arquivo_busca:
                for linha in arquivo_busca:
                    if linha.strip():
                        partes = linha.strip().split("|")
                        id_str = partes[0].replace("Tarefa de numero ","").strip()
                        id_str = int(id_str)
                        if id == id_str:
                            print(linha)
                            return
            print(f"Nenhuma tarefa encontrada com o ID {id}.")
            return
        except ValueError:
            print("Entrada invalida, digite apenas numeros.")

def excluir_todas_tarefas():
    confirmacao = input("Tem certeza que deseja excluir todas as tarefas? [s/n]: ").strip().lower()

    if confirmacao == "s":
        try:
            with open(ROOT_PATH / "tarefas.txt", "w", encoding="utf-8") as arquivo_deletado:
                pass
            print("Todas as tarefas foram deletadas com sucesso.")
        except Exception as e:
            print(f"Não foi possivel excluir todas as tarefas devido ao erro {e}")
    else:
        print("Operação de exclusão cancelada.")

def concluir_tarefa():
    try:
        id = int(input("Digite o numero da tarefa que deseja marcar como concluida: "))
        caminho = ROOT_PATH / "tarefas.txt"

        if not caminho.exists():
            print("Arquivo de tarefas não encontrado.")
        with open (caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        nova_lista = []
        tarefa_encontrada = False
        for linha in linhas:
            if linha.strip():
                partes = linha.strip().split("|")
                id_str = partes[0].replace("Tarefa de numero ", "").strip()
                if int(id_str) == id:
                    if "[CONCLUIDA]" in linha:
                        print("Esta tarefa ja esta marcada como concluida.")
                        return
                    data_atual = datetime.now().strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    linha = linha.strip() + f" [CONCLUIDA] Dia {data_atual} às {hora_atual}.\n"
                    tarefa_encontrada = True
                nova_lista.append(linha)

        if tarefa_encontrada:
            with  open (caminho, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(nova_lista)
            print(f"Tarefa {id} marcada como concluida.")
        else:
            print(f"Tarefa com ID {id} não encontrada.")

    except ValueError:
        print("Entrada invalida, digite apenas numeros.")
    except Exception as e:
        print(f"Ocorreu um erro ao concluir a tarefa: {e}")

while True:
    opcao = menu()

    if opcao == 1:
        nova_tarefa()

    elif opcao == 2:
        listar_tarefas()

    elif opcao == 3:
        buscar_tarefa()

    elif opcao == 4:
        concluir_tarefa()

    elif opcao == 5:
        excluir_todas_tarefas()

    elif opcao == 0:
        print("Saindo do sistema, até a proxima :)")
        break

    else:
        print("Opcao invalida.")