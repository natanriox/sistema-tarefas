import uuid
from datetime import datetime
from typing import List, Dict, Optional


class Tarefa:
    def __init__(self, titulo: str, descricao: str, prioridade: int):
        self.id = str(uuid.uuid4())[:8]
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.data_conclusao: Optional[str] = None

    def marcar_concluida(self):
        self.concluida = True
        self.data_conclusao = datetime.now().strftime("%d/%m/%Y %H:%M")

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade,
            'concluida': self.concluida,
            'data_criacao': self.data_criacao,
            'data_conclusao': self.data_conclusao,
        }

    @classmethod
    def from_dict(cls, data: Dict):
        tarefa = cls(data['titulo'], data['descricao'], data.get('prioridade', 0))
        tarefa.id = data.get('id', tarefa.id)
        tarefa.concluida = data.get('concluida', False)
        tarefa.data_criacao = data.get('data_criacao', tarefa.data_criacao)
        tarefa.data_conclusao = data.get('data_conclusao', None)
        return tarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas: List[Tarefa] = []

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return

        print("\nSuas Tarefas:")
        print("-" * 80)
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{i}. {status} [{tarefa.prioridade}] {tarefa.titulo}")
            print(f"   {tarefa.descricao}")
            print(f"   Criada: {tarefa.data_criacao}")
            if tarefa.concluida and tarefa.data_conclusao:
                print(f"   Concluída: {tarefa.data_conclusao}")
            print()

    def marcar_concluida(self):
        self.listar_tarefas()
        if not self.tarefas:
            return

        try:
            id_tarefa = input("\nID da tarefa a concluir: ").strip()
            for tarefa in self.tarefas:
                if tarefa.id == id_tarefa:
                    tarefa.marcar_concluida()
                    print("Tarefa marcada como concluída.")
                    return
            print("Tarefa não encontrada.")
        except Exception:
            print("Erro ao processar.")

    def remover_tarefa(self):
        self.listar_tarefas()
        if not self.tarefas:
            return

        try:
            id_tarefa = input("\nID da tarefa a remover: ").strip()
            original = len(self.tarefas)
            self.tarefas = [t for t in self.tarefas if t.id != id_tarefa]
            if len(self.tarefas) < original:
                print("Tarefa removida.")
            else:
                print("Tarefa não encontrada.")
        except Exception:
            print("Erro ao remover.")

    def relatorio(self):
        total = len(self.tarefas)
        concluidas = len([t for t in self.tarefas if t.concluida])
        pendentes = total - concluidas
        progresso = (concluidas / total * 100) if total else 0.0

        print("\nRelatório:")
        print("=" * 40)
        print(f"Total de tarefas: {total}")
        print(f"Concluídas: {concluidas}")
        print(f"Pendentes: {pendentes}")
        print(f"Progresso: {progresso:.1f}%")




    