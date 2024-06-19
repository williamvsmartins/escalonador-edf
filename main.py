import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from task import Task
from scheduler import Scheduler

class EDFSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escalonador EDF")
        
        self.task_list = []
        self.style = [
            "status-one", "status-two", "status-three", "status-four", 
            "status-five", "status-six", "status-seven", "status-eight", 
            "status-nine", "status-ten", "status-eleven", "status-twelve"
        ]
        self.style_list = list(self.style)
        
        self.create_widgets()

    def create_widgets(self):
        self.et_label = ttk.Label(self.root, text="ET")
        self.et_label.grid(row=0, column=0)
        
        self.et_entry = ttk.Entry(self.root)
        self.et_entry.grid(row=0, column=1)

        self.period_label = ttk.Label(self.root, text="Período")
        self.period_label.grid(row=0, column=2)

        self.period_entry = ttk.Entry(self.root)
        self.period_entry.grid(row=0, column=3)
        
        self.add_button = ttk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=4)
        
        self.lcm_label = ttk.Label(self.root, text="LCM")
        self.lcm_label.grid(row=1, column=0)
        
        self.lcm_value_label = ttk.Label(self.root, text="0")
        self.lcm_value_label.grid(row=1, column=1)
        
        self.schedule_button = ttk.Button(self.root, text="Agendar", command=self.schedule)
        self.schedule_button.grid(row=2, column=4)

        self.task_table = ttk.Treeview(self.root, columns=("ID", "ET", "Período"), show='headings')
        self.task_table.heading("ID", text="ID da Tarefa")
        self.task_table.heading("ET", text="ET")
        self.task_table.heading("Período", text="Período")
        self.task_table.grid(row=3, column=0, columnspan=5)
        
    def add_task(self):
        try:
            et = int(self.et_entry.get())
            period = int(self.period_entry.get())
            task = Task(et, period)
            self.task_list.append(task)
            self.task_table.insert("", "end", values=(task.name, task.et, task.period))
            self.et_entry.delete(0, tk.END)
            self.period_entry.delete(0, tk.END)
            self.lcm_value_label.config(text=str(Scheduler.calc_lcm(self.task_list)))
        except ValueError:
            messagebox.showerror("Entrada Inválida", "Por favor, insira valores válidos para ET e Período")

    def schedule(self):
        if not self.task_list:
            messagebox.showwarning("Nenhuma Tarefa", "Por favor, adicione tarefas antes de agendar")
            return

        self.style_list = list(self.style)
        scheduled_tasks, deadlines_list = Scheduler.schedule(self.task_list)
        self.fill_table(scheduled_tasks, deadlines_list)
        self.draw_chart(scheduled_tasks)
        
    def fill_table(self, scheduled_tasks, deadlines_list):
        for i, task in enumerate(scheduled_tasks):
            task_name = task.name if task else "ocioso"
            deadlines = ", ".join(str(t) for t in deadlines_list[i])
            print(f"Tempo: {i}, Tarefa: {task_name}, Deadlines: {deadlines}")
        
    def draw_chart(self, scheduled_tasks):
        fig, ax = plt.subplots()
        y_ticks = []
        for i, task in enumerate(self.task_list):
            y_ticks.append(task.name)
            for j, scheduled_task in enumerate(scheduled_tasks):
                if task == scheduled_task:
                    ax.broken_barh([(j, 1)], (i * 10, 9), facecolors=self.get_random_color())

        ax.set_yticks(range(5, len(self.task_list) * 10, 10))
        ax.set_yticklabels(y_ticks)
        ax.set_xlabel('Tempo')
        ax.set_title('Escalonamento EDF - Earliest Deadline First')
        plt.show()

    def get_random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))


if __name__ == "__main__":
    root = tk.Tk()
    app = EDFSchedulerApp(root)
    root.mainloop()
