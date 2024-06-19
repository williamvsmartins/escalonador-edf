from collections import defaultdict

class Scheduler:
    @staticmethod
    def schedule(task_list):
        lcm = Scheduler.calc_lcm(task_list)
        scheduled_tasks = []
        deadlines_list = defaultdict(list)
        waiting_map = defaultdict(list)

        for time_unit in range(lcm):
            for task in task_list:
                if time_unit % task.period == 0:
                    for _ in range(task.et):
                        waiting_map[time_unit + task.period].append(task)
                    deadlines_list[time_unit].append(task)

            if waiting_map:
                min_key = min(waiting_map.keys())
                scheduled_tasks.append(waiting_map[min_key].pop(0))
                if not waiting_map[min_key]:
                    del waiting_map[min_key]
            else:
                scheduled_tasks.append(None)

        return scheduled_tasks, deadlines_list

    @staticmethod
    def calc_lcm(task_list):
        lcm = task_list[0].period
        while any(lcm % task.period != 0 for task in task_list):
            lcm += 1
        return lcm
