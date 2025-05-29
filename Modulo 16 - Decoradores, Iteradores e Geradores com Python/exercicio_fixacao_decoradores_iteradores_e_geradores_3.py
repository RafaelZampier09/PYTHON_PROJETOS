"""
Desafio Final - Gerenciador de Processos com Falhas Aleatórias

Objetivo:
Simular a execução de uma fila de processos, onde cada processo passa por etapas e pode falhar aleatoriamente.
Use:
- Classes com __iter__ e __next__ (iteradores)
- Geradores para etapas de execução
- Decoradores para log de execução
- time.sleep() para simular tempo real
- random para simular falhas
- try/except para tratar exceções

Extra:
- Um processo pode falhar na etapa "Processando"
- O decorador deve registrar falha caso ocorra
"""
import functools
import random
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
        try:
            for resultado in funcao(*args, **kwargs):
                yield resultado
                time.sleep(1)
            print(f"[LOG] Finalizando a execução de: {nome}\n")
        except Exception as erro:
            print(f"[ERRO] Processo '{nome}' falhou: {erro}")
            print(f"[LOG] Finalizando a execução de:{nome} com erro\n")
    return executar

@log_execucao
def executar_processo(processo):
    yield f"Executando: {processo}"
    yield f"Iniciando {processo}"
    if processo == "Chrome":
        yield f"Abrindo multiplas abas"
    elif processo == "Word":
        yield f"Abrindo documentação"
    elif processo == "VsCode":
        yield f"Carregando extensões"
    if random.choice([True, False]):
        raise Exception("Falha durante o processamento.")
    yield f"Processando {processo}"
    yield f"Finalizando {processo}"
    yield f"Finalizou: {processo}"

processo = GerenciadorProcessos(processos)

for processo_nome in processo:
    for etapa in executar_processo(processo_nome):
        print(etapa)