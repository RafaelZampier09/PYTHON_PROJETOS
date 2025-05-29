# Exercício: Gerenciador de Processos com Logs e Geradores
# 
# Objetivo:
# - Criar uma classe chamada "GerenciadorProcessos" que recebe uma lista de processos (nomes de programas) e simula sua execução.
# - Cada processo será simulado em etapas: "Inicializando", "Carregando", "Executando", "Encerrando".
# 
# Requisitos:
# 1. Torne a classe iterável (usando __iter__ e __next__) para iterar pelos nomes dos processos.
# 2. Crie uma função decoradora que exibe logs antes e depois da execução de cada processo.
# 3. A função que executa o processo deve usar "yield" para retornar cada etapa.
# 
# Saída esperada (exemplo para o processo 'Chrome'):
# [LOG] Iniciando o processo: Chrome
# Inicializando Chrome
# Carregando Chrome
# Executando Chrome
# Encerrando Chrome
# [LOG] Encerrando o processo: Chrome
# 
# Dica: o padrão é bem parecido com o seu código anterior, mas com nomes diferentes.
import functools
import time

processos = ["Chrome", "Word", "VsCode"]

class GerenciadorProcessos:
    def __init__(self, processos):
        self.processos = processos
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < len(self.processos):
            processo = self.processos[self.contador]
            self.contador += 1
            return processo
        else:
            raise StopIteration
        

def log_execucao(funcao):
    @functools.wraps(funcao)
    def executar(*args, **kwargs):
        nome = args[0]
        print(f"[LOG] Iniciando a execução de: {nome}")
        for resultado in funcao(*args, **kwargs):
            yield resultado
        print(f"[LOG] Finalizando a execução de: {nome}\n")
    return executar

@log_execucao
def executar_processo(processo):
    yield f"Executando: {processo}"
    time.sleep(1)
    yield f"Iniciando {processo}"
    time.sleep(1)
    if processo == "Chrome":
        yield f"Abrindo multiplas abas"
    elif processo == "Word":
        yield f"Abrindo documentação"
    elif processo == "VsCode":
        yield f"Carregando extensões"
    time.sleep(1)
    yield f"Processando {processo}"
    time.sleep(1)
    yield f"Finalizando {processo}"
    time.sleep(1)
    yield f"Finalizou: {processo}"
    time.sleep(1)

processo = GerenciadorProcessos(processos)

for processo_nome in processo:
    for etapa in executar_processo(processo_nome):
        print(etapa)
        