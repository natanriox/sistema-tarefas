from models import Tarefa, GerenciadorTarefas
from utils import salvar_dados, carregar_dados
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    gerenciador = GerenciadorTarefas()


    while True:
        limpar_tela()
        print("Sistema de Gerenciamento de Tarefas")
        print("=" * 50)
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Concluída")
        print("4. Remover Tarefa")
        print("5. Relatório")
        print("6. Salvar e Sair")
        print("-" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição")
            prioridade = input("Prioridade (1-5): ")
            gerenciador.adicionar_tarefa(titulo, descricao, int(prioridade))
            input("\nTarefa gerada! Pressione qualquer tecla para continuar...")

        elif opcao == "2":
            gerenciador.marcar_concluida()
            input("\nPressione qualquer tecla para continuar...")

        elif opcao == "3":
            gerenciador.marcar_concluida()
            input("\nPressione qualquer tecla para continuar...")

        elif opcao == "4":
            gerenciador.remover_tarefa()
            input("\nPressione qualquer tecla para continuar...")

        elif opcao == "6":
            salvar_dados(gerenciador.tarefas)
            print("Dados salvos.")
            break

if __name__ == "--main--":
    menu_principal()
        