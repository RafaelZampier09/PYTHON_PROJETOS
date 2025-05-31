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
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()
ROOT_PATH = Path(__file__).parent

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    console.print(Panel.fit(
        """[bold cyan]
[1] ADICIONAR TAREFA
[2] LISTAR TAREFAS
[3] BUSCAR TAREFA
[4] CONCLUIR TAREFA
[5] EXCLUIR TODAS TAREFAS
[0] SAIR[/bold cyan]""",
        title="[bold green]MENU DE OPÇÕES",
        subtitle="Escolha uma opção",
        border_style="bright_magenta"
    ))

    try:
        return int(console.input("[bold yellow]→ Sua escolha: [/bold yellow]"))
    except ValueError:
        console.print("[bold red]Entrada inválida! Digite um número.[/bold red]")
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
            tarefa = console.input("[bold yellow]📝 Digite uma nova tarefa: [/bold yellow]").strip()

            if not tarefa:
                console.print("[bold red]⚠️ A tarefa não pode estar vazia.[/bold red]")
                continue

            data_atual = datetime.now().strftime("%d/%m/%Y")
            hora_atual = datetime.now().strftime("%H:%M:%S")

            with open(ROOT_PATH / "tarefas.txt", "a", newline="", encoding="utf-8") as arquivo:
                arquivo.write(f"Tarefa de numero {id_tarefa} | Nome: {tarefa} | Horário/data de registro: {data_atual} às {hora_atual}\n")

            console.print(Panel.fit(
                f"[bold green]✅ Tarefa registrada com sucesso![/bold green]\n\n"
                f"[cyan]ID:[/] {id_tarefa}\n"
                f"[yellow]Nome:[/] {tarefa}\n"
                f"[magenta]Data/Hora:[/] {data_atual} às {hora_atual}",
                title="Nova Tarefa", border_style="bright_blue"
            ))
            return

        except Exception as exc:
            console.print(f"[bold red]❌ Entrada inválida. Tente novamente.[/bold red]\n[dim]{exc}[/dim]")

def listar_tarefas():
    caminho = ROOT_PATH / "tarefas.txt"

    if not caminho.exists():
        console.print("[bold red]Arquivo de tarefas não encontrado.[/bold red]")
        return

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]

            if not linhas:
                console.print("[bold yellow]Nenhuma tarefa registrada até o momento.[/bold yellow]")
                return

            tabela = Table(title="Lista de Tarefas", show_lines=True)

            tabela.add_column("ID", style="cyan", justify="center")
            tabela.add_column("Nome", style="green")
            tabela.add_column("Data/Hora de Registro", style="magenta")
            tabela.add_column("Status", style="bold")
            tabela.add_column("Data/Hora da Conclusão", style="bold green")

            for linha in linhas:
                partes = linha.split("|")
                id_str = partes[0].replace("Tarefa de numero ", "").strip()
                nome = partes[1].replace("Nome: ", "").strip()
                data_hora_registro = partes[2].replace("Horário/data de registro: ", "").strip()

                if "[CONCLUIDA]" in linha:
                    status = "✅ Concluída"
                    # Extrai a data/hora da conclusão que vem depois de "[CONCLUIDA]"
                    data_conclusao = linha.split("[CONCLUIDA]")[-1].strip()
                else:
                    status = "🕒 Pendente"
                    data_conclusao = ""

                tabela.add_row(id_str, nome, data_hora_registro, status, data_conclusao)

            console.print(tabela)

    except Exception as e:
        console.print(f"[bold red]Erro ao ler tarefas: {e}[/bold red]")


def buscar_tarefa():
    caminho = ROOT_PATH / "tarefas.txt"

    if not caminho.exists():
        console.print("[bold red]Não temos nenhuma tarefa até o momento.[/bold red]")
        return

    try:
        id = int(console.input("[bold yellow]Digite o número da tarefa que deseja buscar: [/bold yellow]"))

        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip():
                    partes = linha.strip().split("|")
                    id_str = partes[0].replace("Tarefa de numero ", "").strip()

                    if int(id_str) == id:
                        nome = partes[1].replace("Nome: ", "").strip()
                        data_hora_registro = partes[2].replace("Horário/data de registro: ", "").strip()

                        if "[CONCLUIDA]" in linha:
                            status = "✅ Concluída"
                            data_hora_conclusao = linha.split("[CONCLUIDA]")[-1].strip()
                        else:
                            status = "🕒 Pendente"
                            data_hora_conclusao = "Não concluído"

                        conteudo = Text()
                        conteudo.append(f"ID: {id_str}\n", style="bold cyan")
                        conteudo.append(f"Nome: {nome}\n", style="bold green")
                        conteudo.append(f"Data/hora de registro: {data_hora_registro}\n", style="bold magenta")
                        conteudo.append(f"Status: {status}\n", style="bold yellow" if status == "🕒 Pendente" else "bold green")
                        conteudo.append(f"Data/hora de conclusão: {data_hora_conclusao}", style="bold magenta")

                        console.print(Panel(conteudo, title="[bold orange1]🔍 RESULTADO DA BUSCA[/bold orange1]", expand=False))
                        return

        console.print(f"[bold red]Nenhuma tarefa encontrada com o ID {id}.[/bold red]")

    except ValueError:
        console.print("[bold red]Entrada inválida. Digite apenas números.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Erro ao buscar tarefa: {e}[/bold red]")


def excluir_todas_tarefas():
    confirmacao = console.input("[bold #FF4500]⚠️ Tem certeza que deseja excluir todas as tarefas? {s/n}: [/bold #FF4500]").strip().lower()

    if confirmacao == "s":
        try:
            with open(ROOT_PATH / "tarefas.txt", "w", encoding="utf-8"):
                pass
            console.print(Panel("[bold green]✅ Todas as tarefas foram deletadas com sucesso.[/bold green]",
                                border_style="green", title="Sucesso", padding=(1, 2)))
        except Exception as e:
            console.print(Panel(f"[bold red]❌ Não foi possível excluir as tarefas.[/bold red]\n[dim]{e}[/dim]",
                                border_style="red", title="Erro", padding=(1, 2)))
    else:
        console.print(Panel("[yellow]🚫 Operação de exclusão cancelada.[/yellow]",
                            border_style="yellow", title="Cancelado", padding=(1, 2)))

def concluir_tarefa():
    try:
        id = int(console.input("[bold yellow]📝 Digite o número da tarefa que deseja marcar como concluída: [/bold yellow]"))
        caminho = ROOT_PATH / "tarefas.txt"

        if not caminho.exists():
            console.print(Panel("📁 [bold red]Arquivo de tarefas não encontrado.[/bold red]", border_style="red"))
            return

        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        nova_lista = []
        tarefa_encontrada = False
        for linha in linhas:
            if linha.strip():
                partes = linha.strip().split("|")
                id_str = partes[0].replace("Tarefa de numero ", "").strip()
                if int(id_str) == id:
                    if "[CONCLUIDA]" in linha:
                        console.print(Panel(f"⚠️ [yellow]A tarefa {id} já está marcada como concluída.[/yellow]", border_style="yellow"))
                        return
                    data_atual = datetime.now().strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    linha = linha.strip() + f" [CONCLUIDA] Dia {data_atual} às {hora_atual}.\n"
                    tarefa_encontrada = True
                nova_lista.append(linha)

        if tarefa_encontrada:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(nova_lista)
            console.print(Panel(f"✅ [bold green]Tarefa {id} marcada como concluída.[/bold green]", border_style="green"))
        else:
            console.print(Panel(f"🔍 [bold yellow]Tarefa com ID {id} não encontrada.[/bold yellow]", border_style="yellow"))

    except ValueError:
        console.print(Panel("[red]❌ Entrada inválida. Digite apenas números.[/red]", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[bold red]❌ Ocorreu um erro ao concluir a tarefa:[/bold red]\n[dim]{e}[/dim]", border_style="red"))


while True:
    opcao = menu()

    if opcao == 1:
        limpar_tela()
        nova_tarefa()

    elif opcao == 2:
        limpar_tela()
        listar_tarefas()

    elif opcao == 3:
        limpar_tela()
        buscar_tarefa()

    elif opcao == 4:
        limpar_tela()
        concluir_tarefa()

    elif opcao == 5:
        limpar_tela()
        excluir_todas_tarefas()

    elif opcao == 0:
        console.print("[bold green]👋 Saindo do sistema, até a próxima![/bold green]")
        break

    else:
        print("")
