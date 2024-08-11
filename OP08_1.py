import tkinter as tk


def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)


def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        # task_listBox.itemconfig(selected_task, bg="DodgerBlue4")
        for i in selected_task:  # task_listBox.delete(selected_task):
            task_text = task_listBox.get(i)
            end_task_listbox.insert(tk.END, task_text)
            task_listBox.delete(i)


root = tk.Tk()
root.title("Список задач")
root.geometry("400x600")
root.configure(background="snow3")

text_1 = tk.Label(root, text="Введите вашу задачу:", fg="Black", bg="snow3")
text_1.pack(pady=(15, 5))

task_entry = tk.Entry(root, width=30, bg="MintCream")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу.", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Удалить задачу.", command=delete_task)
delete_task_button.pack(pady=5)

mark_button = tk.Button(root, text="Перенести выполненную задачу.", command=mark_task)
mark_button.pack(pady=5)

frame = tk.Frame(root)
frame.pack(fill=tk.X)
frame.configure(bg="SlateGray")

text_2 = tk.Label(frame, text="Список текущих задач:", fg="Black", bg="SlateGray")
text_2.pack(side="left", padx=20, pady=5)

text_3 = tk.Label(frame, text="Список завершенных задач:", fg="Black", bg="SlateGray")
text_3.pack(side="right", padx=20, pady=5)

# frame1 = tk.Frame(root)
# frame1.pack(fill=tk.X)

task_listBox = tk.Listbox(root, height=20, width=20, bg="snow4")
task_listBox.pack(side="left", fill="both", expand=True)

# cur_task_listbox = tk.Listbox(root,height=20, width=20,bg="DeepPink1")
# cur_task_listbox.pack(side="left", pady=5, padx=5)

end_task_listbox = tk.Listbox(root, height=20, width=20, bg="snow4")
end_task_listbox.pack(side="right", fill="both", expand=True)


root.mainloop()