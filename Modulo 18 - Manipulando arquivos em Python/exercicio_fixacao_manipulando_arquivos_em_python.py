"""
📄 Descrição:

Crie um script em Python que funcione como um gerenciador de notas simples. 
O programa deve permitir gravar, listar, buscar e excluir notas salvas em um arquivo de texto chamado "notas.txt".

✅ Funcionalidades obrigatórias:

1. Criar uma nova nota e salvar no arquivo.
2. Listar todas as notas existentes.
3. Buscar uma nota específica por palavra-chave.
4. Excluir todas as notas (com confirmação).
5. Usar 'with' para manipular arquivos com segurança.
6. Utilizar 'Path' do módulo pathlib para lidar com caminhos.
7. (Extra) Verificar se o arquivo já existe antes de ler.

Dica: cada nota pode ser salva em uma nova linha no arquivo.

Exemplo de menu:
[1] Nova nota
[2] Listar notas
[3] Buscar nota
[4] Excluir todas as notas
[0] Sair

"""
from pathlib import Path

ROOT_PATH = Path(__file__).parent
def menu ():
    print ("""
    ========= MENU =========
    [1] Nova nota
    [2] Listar notas
    [3] Buscar notas
    [4] Excluir todas as notas
    [0] Sair
""")
    
    try:
        return int(input("Escolha uma opção =>  "))
    except ValueError:
        print("Opção invalida, digite apenas numeros.")
        return 0
    
    
def proximo_id():
    caminho = ROOT_PATH / "notas.txt"

    if not caminho.exists():
        return 1  # Verifica se o caminho existe, caso negativo, retorna 1, pois sera a primeira nota
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo: # Abre o arquivo por leitura
        linhas = arquivo.readlines() # lista de todas as linhas do arquivo
        if not linhas:
            return 1 # Significa que não tem nenhuma nota registrada ainda
        ultima_linha = linhas[-1] # Pega a ultima linha do arquivo (ultimo ID)
        try:
            # split pega toda a parte antes do |
            # replace substitui a parte do ID = por um espaço vazio
            # strip remove os espaços em branco
            id_str = ultima_linha.split("|")[0].replace("ID = ", "").strip()
            # retorna o id_str como inteiro e acrescenta mais 1
            return int(id_str) + 1
        except:
            return 1
        

def nova_nota():
    id_nota = proximo_id()
    while True:
        try:
            nota = float(input("Digite a nota (somente numeros): "))
            with open(ROOT_PATH / "notas.txt", "a", newline="", encoding="utf-8") as arquivo:
                arquivo.write(f"ID = {id_nota}| Nota = {nota}\n")
            print(f"Nota {nota} registrada com sucesso com o ID: {id_nota}")
            return
        except ValueError:
            print("Entrada invalida, digite apenas números...")
        

def listar_notas():
    try:
        with open(ROOT_PATH / "notas.txt", "r", newline="", encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
            if not linhas:
                print("Nenhuma nota registrada.")
                return
            for linha in linhas:
                print(linha)
                print("-" * 30)
    except FileNotFoundError:
        print("Arquivo de notas não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler notas: {e}")
            

def buscar_nota():
    while True:
        try:
            id = int(input("Digite o ID da nota que deseja buscar: "))
            with open(ROOT_PATH / "notas.txt", "r", newline="", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    if linha.strip():
                        partes = linha.strip().split("|")
                        id_str = partes[0].replace("ID = ", "").strip()
                        nota_str = partes[1].replace("Nota = ", "").strip()
                        id_str = int(id_str)
                        if id == id_str:
                            print(f"A nota do ID {id} é igual: {nota_str}")
                            return
            print(f"Nenhuma nota encontrada com o ID {id}")
            return
        except ValueError:
            print("Entrada invalida, digite apenas numeros")


def excluir_todas_notas():
    confirmacao = input("Tem certeza que deseja excluir todas as notas? [s/n]: ").strip().lower()

    if confirmacao == "s":
        try:
            with open(ROOT_PATH / "notas.txt", "w", encoding="utf-8") as arquivo:
                pass
            print("Todas as notas foram excluidas com sucesso.")
        except Exception as e:
            print(f"Não foi possivel excluir as notas devido ao erro {e}")
    else:
        print("Operação de exclusão cancelada.")

while True:
    opcao = menu()

    if opcao == 1:
        nova_nota()

    elif opcao == 2:
        listar_notas()

    elif opcao == 3:
        buscar_nota()

    elif opcao == 4:
        excluir_todas_notas()

    elif opcao == 0:
        print("Saindo do sistema, até a proxima :)")
        break

    else:
        print("Opção invalida.")

