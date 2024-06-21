from collections import defaultdict

# Classe Scheduler para gerenciar o escalonamento das tarefas
class Scheduler:
    @staticmethod
    def schedule(task_list):
        # Calcula o Mínimo Múltiplo Comum (LCM) dos períodos das tarefas
        lcm = Scheduler.calc_lcm(task_list)
        # Lista para armazenar as tarefas agendadas
        scheduled_tasks = []
        # Dicionário para armazenar os deadlines das tarefas
        deadlines_list = defaultdict(list)
        # Mapa de espera para gerenciar as tarefas que estão aguardando execução
        waiting_map = defaultdict(list)

        # Loop sobre cada unidade de tempo até o LCM
        for time_unit in range(lcm):
            # Verifica cada tarefa na lista de tarefas
            for task in task_list:
                # Se a unidade de tempo é um múltiplo do período da tarefa, adiciona a tarefa ao mapa de espera
                if time_unit % task.period == 0:
                    for _ in range(task.et):
                        waiting_map[time_unit + task.period].append(task)
                    # Adiciona a tarefa à lista de deadlines
                    deadlines_list[time_unit].append(task)

            # Se há tarefas no mapa de espera, agenda a tarefa com o menor deadline
            if waiting_map:
                min_key = min(waiting_map.keys())
                scheduled_tasks.append(waiting_map[min_key].pop(0))
                # Remove a chave do mapa de espera se não houver mais tarefas para aquele deadline
                if not waiting_map[min_key]:
                    del waiting_map[min_key]
            else:
                # Adiciona None para indicar que o processador está ocioso nessa unidade de tempo
                scheduled_tasks.append(None)

        return scheduled_tasks, deadlines_list

    @staticmethod
    def calc_lcm(task_list):
        # Calcula o Mínimo Múltiplo Comum (LCM) dos períodos das tarefas na lista
        lcm = task_list[0].period
        while any(lcm % task.period != 0 for task in task_list):
            lcm += 1
        return lcm
