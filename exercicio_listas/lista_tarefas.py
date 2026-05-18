tarefas = []

print("=== Lista de Tarefas ===")
print("Digite suas tarefas (digite 'fim' para encerrar):")

while True:
    tarefa = input("Tarefa: ")
    if tarefa.lower() == "fim":
        break
    tarefas.append(tarefa)

print("\n=== Suas Tarefas ===")
if tarefas:
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
else:
    print("Nenhuma tarefa cadastrada.")
