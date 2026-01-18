import json
import os
from models import Tarefa
from typing import List

ARQUIVO_DADOS = "data/tarefas.json"


def criar_pasta_dados():
    os.makedirs(os.path.dirname(ARQUIVO_DADOS) or "data", exist_ok=True)


def salvar_dados(tarefas: List[Tarefa]):
    """Salva a lista de tarefas em JSON (cria a pasta se necessário)."""
    criar_pasta_dados()
    dados = [tarefa.to_dict() for tarefa in tarefas]
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print("Dados salvos com sucesso.")


def carregar_dados() -> List[Tarefa]:
    """Carrega as tarefas do arquivo JSON. Retorna lista vazia se não existir ou erro."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        tarefas = [Tarefa.from_dict(dado) for dado in dados]
        return tarefas
    except Exception:
        print("Erro ao carregar dados. Iniciando com lista vazia.")
        return []


