class Task:
    count = 0  # Variável de classe para contar o número de instâncias de Task

    def __init__(self, et, period):
        self.et = et  # Tempo de execução da tarefa
        self.period = period  # Período da tarefa
        self.id = Task.count  # ID único da tarefa, baseado na contagem de instâncias
        self.name = f"T{Task.count}"  # Nome da tarefa, usando a contagem de instâncias
        Task.count += 1  # Incrementa a contagem de tarefas

    def __str__(self):
        return self.name  # Retorna o nome da tarefa como string
