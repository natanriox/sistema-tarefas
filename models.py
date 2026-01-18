import uuid
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.id = str(uuid.uuid4())[:8]
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = int(prioridade)
        self.concluida = False
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def marcar_concluida(self):
        self.concluida = True
    
    def to_dict(self):
        return self.__dict__

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, titulo, descricao, prioridade):
        tarefa = Tarefa(titulo, descricao, prioridade)
        self.tarefas.append(tarefa)
        print(f" Tarefa '{titulo}' adicionada!")  # ← CORRIGIDO!
    
    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa!")
            return
        for i, t in enumerate(self.tarefas, 1):
            status = "Concluída" if t.concluida else "⏳"
            print(f"{i}. {status} [{t.prioridade}] {t.titulo}")
            print(f"   {t.descricao}")
    
    def marcar_concluida(self):
        self.listar_tarefas()
        id_t = input("ID: ")
        for t in self.tarefas:
            if t.id == id_t:
                t.marcar_concluida()
                print("Marcada!")
                return
        print("Não encontrada!")
    
    def remover_tarefa(self):
        self.listar_tarefas()
        id_t = input("ID: ")
        self.tarefas = [t for t in self.tarefas if t.id != id_t]
        print("Removida!")
    
    def relatorio(self):
        total = len(self.tarefas)
        concl = len([t for t in self.tarefas if t.concluida])
        print(f"Total: {total} | Concluídas {concl} | Total {concl/total*100:.0f}%" if total else "Sem tarefas")
