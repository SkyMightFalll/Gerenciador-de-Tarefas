import time
import json
import os
    
ARQUIVO_TAREFAS = "tarefas.json"

#CARREGAR TAREFAS

if os.path.exists(ARQUIVO_TAREFAS):
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []


#FUNÇÃO PARA SALVAR

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


#GERENCIADOR DE TAREFAS

while True:
    time.sleep(2)

    print()
    print("----------------------------------")
    print("===== GERENCIADOR DE TAREFAS =====")
    print("[1] - Adicionar Tarefa")
    print("[2] - Listar Tarefas")
    print("[3] - Concluir Tarefa")
    print("[4] - Excluir Tarefa")
    print("[0] - Sair do Programa")

    print()

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número inteiro válido.")
        continue

    print()

    match escolha:

        case 1:
            descricao = input("Digite sua tarefa: ").strip()

            if not descricao:
                print("A descrição não pode ficar vazia.")
                continue

            tarefa = {
                "descricao": descricao,
                "status": False
            }

            tarefas.append(tarefa)
            salvar_tarefas()

            print("Tarefa adicionada com sucesso!")

        case 2:
            if not tarefas:
                print("Sem tarefas no momento.")
            else:
                print("===== MINHAS TAREFAS =====")
                print()

                for i, tarefa in enumerate(tarefas):
                    status = (
                        "[CONCLUÍDA]"
                        if tarefa["status"]
                        else "[PENDENTE]"
                    )

                    print(
                        f"ID[{i}] - "
                        f"Tarefa: {tarefa['descricao']} "
                        f"{status}"
                    )

        case 3:
            if not tarefas:
                print("Sem tarefas no momento.")
            else:
                print("===== MINHAS TAREFAS =====")
                print()

                for i, tarefa in enumerate(tarefas):
                    status = (
                        "[CONCLUÍDA]"
                        if tarefa["status"]
                        else "[PENDENTE]"
                    )

                    print(
                        f"ID[{i}] - "
                        f"Tarefa: {tarefa['descricao']} "
                        f"{status}"
                    )

                try:
                    print()
                    id_concluir = int(
                        input("Digite o ID da tarefa que deseja concluir: ")
                    )

                    if 0 <= id_concluir < len(tarefas):
                        if tarefas[id_concluir]["status"]:
                            print("Esta tarefa já foi concluída!")
                        else:
                            tarefas[id_concluir]["status"] = True
                            salvar_tarefas()

                            print("Tarefa concluída com sucesso!")
                    else:
                        print("Número de ID inválido.")

                except ValueError:
                    print("Digite um número inteiro válido.")

        case 4:
            if not tarefas:
                print("Sem tarefas no momento.")
            else:
                print("===== MINHAS TAREFAS =====")
                print()

                for i, tarefa in enumerate(tarefas):
                    status = (
                        "[CONCLUÍDA]"
                        if tarefa["status"]
                        else "[PENDENTE]"
                    )

                    print(
                        f"ID[{i}] - "
                        f"Tarefa: {tarefa['descricao']} "
                        f"{status}"
                    )

                try:
                    print()
                    id_exclusao = int(
                        input("Digite o ID da tarefa que deseja excluir: ")
                    )

                    if 0 <= id_exclusao < len(tarefas):
                        tarefas.pop(id_exclusao)
                        salvar_tarefas()

                        print("Tarefa excluída com sucesso!")
                    else:
                        print("Número de ID inválido.")

                except ValueError:
                    print("Digite um número inteiro válido.")

        case 0:
            print("Saindo do programa...")
            break

        case _:
            print("Valor inválido.")
