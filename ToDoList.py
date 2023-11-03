import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        root.configure(bg='#000000')

        self.tasks = []

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master,text ="Add Task:", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(master)
        self.task_list.pack()

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
    

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.task_list.insert(tk.END,task)
        self.task_entry.delete(0,tk.END)
        with open("data1.txt",'a') as file:
            file.write(task)
            file.seek(0)
            file.close()


    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            del self.tasks[task_index]
            self.task_list.delete(task_index)
        with open("data1.txt",'r+') as file:
            new_file = file.readlines()
            file.seek(0)
            for line in new_file:
                item = str(look)
                if item not in line:
                    file.write(line)
            file.truncate()





root = tk.Tk()
my_todo_list = ToDoList(root)
root.mainloop()