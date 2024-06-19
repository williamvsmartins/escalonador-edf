class Task:
    count = 0

    def __init__(self, et, period):
        self.et = et
        self.period = period
        self.id = Task.count
        self.name = f"T{Task.count}"
        Task.count += 1

    def __str__(self):
        return self.name
