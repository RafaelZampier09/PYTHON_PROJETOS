from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo: # Tudo que esta no with é finalizado quando termina o bloco
        print(arquivo.read())

except FileNotFoundError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilizando python")
except Exception:
    pass