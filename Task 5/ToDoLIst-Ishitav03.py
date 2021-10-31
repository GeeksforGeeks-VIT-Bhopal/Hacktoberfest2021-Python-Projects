import tkinter as tk
import tkinter.messagebox
import pickle

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message="Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning(title="Warning!", message="Please select a task.")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tk.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

root = tk.Tk()
root.title("To-Do List")

#creating GUI
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg='BlanchedAlmond')
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set, bg='Coral')
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, bg= 'Beige')
entry_task.pack()

#button to add tasks
btn_add = tk.Button(root, text="Add task", width=48, command=add_task, bg='Coral')
btn_add.pack()

#button to delete tasks
btn_del = tk.Button(root, text="Delete task", width=48, command=delete_task, bg='Coral')
btn_del.pack()

#button to load saved tasks
btn_load = tk.Button(root, text="Load tasks", width=48, command=load_task, bg='Coral')
btn_load.pack()

#button to save tasks
btn_save = tk.Button(root, text="Save tasks", width=48, command=save_task, bg='Coral')
btn_save.pack()

root.mainloop()