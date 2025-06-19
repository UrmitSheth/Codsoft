# Urmit_Sheth 
# Task-1 : To-Do List
import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f7")

        self.tasks = load_tasks()

        tk.Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

        self.entry_task = tk.Entry(root, width=45, font=("Arial", 12))
        self.entry_task.pack(pady=5)

        btn_frame = tk.Frame(root, bg="#f0f4f7")
        btn_frame.pack(pady=10)

        btn_style = {"width": 12, "font": ("Arial", 10), "bg": "#007acc", "fg": "white", "bd": 0, "relief": tk.FLAT}

        self.btn_add = tk.Button(btn_frame, text="Add Task", command=self.add_task, **btn_style)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_edit = tk.Button(btn_frame, text="Edit Task", command=self.edit_task, **btn_style)
        self.btn_edit.grid(row=0, column=1, padx=5)

        self.btn_done = tk.Button(btn_frame, text="Toggle Done", command=self.toggle_done, **btn_style)
        self.btn_done.grid(row=0, column=2, padx=5)

        self.btn_delete = tk.Button(btn_frame, text="Delete Task", command=self.delete_task, **btn_style)
        self.btn_delete.grid(row=0, column=3, padx=5)

        self.listbox = tk.Listbox(root, width=70, height=12, font=("Arial", 11), selectbackground="#a3d2ca")
        self.listbox.pack(pady=10)

        self.update_listbox()

    def add_task(self):
        task = self.entry_task.get().strip()
        if task:
            self.tasks.append({"title": task, "done": False})
            self.entry_task.delete(0, tk.END)
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def edit_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            current_title = self.tasks[idx]["title"]
            new_title = self.entry_task.get().strip()
            if new_title:
                self.tasks[idx]["title"] = new_title
                self.entry_task.delete(0, tk.END)
                self.update_listbox()
                save_tasks(self.tasks)
            else:
                messagebox.showwarning("Input Error", "Enter new task title to update.")
        else:
            messagebox.showwarning("Selection Error", "Select a task to edit.")

    def toggle_done(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]["done"] = not self.tasks[idx]["done"]
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Selection Error", "Select a task to toggle done.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks.pop(idx)
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓ " if task["done"] else ""
            self.listbox.insert(tk.END, status + task["title"])


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
