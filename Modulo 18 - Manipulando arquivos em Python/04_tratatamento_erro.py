from pathlib import Path

try:
    arquivo = open("meu-arquivo.py")
except FileNotFoundError as exc: # Erro quando tenta abrir um arquivo que não existe
    print("Arquivo não encontrado")
    print(exc)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except PermissionError as exc:
    print(f"Não foi possivel abrir o arquivo: {exc}")