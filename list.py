import customtkinter as ctk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(ctk.END, task)
        entry.delete(0, ctk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def toggle_completed(event):
    index = listbox.curselection()
    if index:
        task = listbox.get(index)
        if task.startswith("✓ "):
            task = task[2:]
        else:
            task = "✓ " + task
        listbox.delete(index)
        listbox.insert(index, task)

root = ctk.CustomTk()
root.title("To-Do List App")

frame = ctk.CustomFrame(root)
frame.pack(pady=10)

listbox = ctk.CustomListbox(
    frame,
    height=10,
    bd=0,
    font=("Courier New", 12),
    selectbackground="#a6a6a6"
)

listbox.bind("<Double-Button-1>", toggle_completed)
listbox.pack(side=ctk.LEFT, fill=ctk.BOTH)

scrollbar = ctk.CustomScrollbar(frame)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = ctk.CustomEntry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)

button_frame = ctk.CustomFrame(root)
button_frame.pack(pady=10)

add_button = ctk.CustomButton(
    button_frame,
    text="Add Task",
    command=add_task,
    font=("Courier New", 12)
)
add_button.pack(side=ctk.LEFT)

delete_button = ctk.CustomButton(
    button_frame,
    text="Delete Task",
    command=delete_task,
    font=("Courier New", 12)
)
delete_button.pack(side=ctk.LEFT)

root.mainloop()
