# Crie uma lista tarefas.
# Adicione três tarefas (strings) a ela.
# Remova a segunda tarefa.
# Imprima o número de tarefas restantes usando len().

# [append;pop;remove;len]

tarefas = []
tarefas.append("Estudar Python")
tarefas.append("Fazer exercícios")
tarefas.append("Revisar conceitos")
tarefas.pop(1)
tarefas.remove("Revisar conceitos")
print(len(tarefas))