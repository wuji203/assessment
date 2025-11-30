# feature1.py - Feature 1: Add sub-tasks and show list
import tkinter as tk
from tkinter import ttk, messagebox

def setup(app):
    app.tasks = []
    app.current_idx = 0

    tk.Label(app, text="Team Meeting Timer", font=("Helvetica", 20, "bold")).pack(pady=20)

    # Task list
    app.tree = ttk.Treeview(app, columns=("Task","Min"), show="headings", height=12)
    app.tree.heading("Task", text="Sub-task")
    app.tree.heading("Min", text="Minutes")
    app.tree.column("Task", width=480)
    app.tree.column("Min", width=100, anchor="center")
    app.tree.pack(padx=30, pady=10)

    # Add task
    frame = tk.Frame(app)
    frame.pack(pady=10)
    tk.Label(frame, text="Task:").grid(row=0, column=0, padx=5)
    app.task_entry = tk.Entry(frame, width=50)
    app.task_entry.grid(row=0, column=1, padx=5)
    tk.Label(frame, text="Min:").grid(row=0, column=2, padx=5)
    app.min_entry = tk.Entry(frame, width=10)
    app.min_entry.grid(row=0, column=3, padx=5)
    tk.Button(frame, text="Add Task", bg="green", fg="white",
              command=lambda: add_task(app)).grid(row=0, column=4, padx=10)

    # Timer display (used by feature3)
    app.timer_label = tk.Label(app, text="00:00", font=("Helvetica", 60, "bold"), fg="blue")
    app.timer_label.pack(pady=30)
    app.name_label = tk.Label(app, text="", font=("Helvetica", 18))
    app.name_label.pack()

def add_task(app):
    name = app.task_entry.get().strip()
    try:
        mins = int(app.min_entry.get())
        if mins <= 0: raise ValueError
    except:
        messagebox.showerror("Error", "Enter valid name and minutes")
        return
    app.tasks.append((name, mins))
    refresh(app)
    app.task_entry.delete(0, tk.END)
    app.min_entry.delete(0, tk.END)

def refresh(app):
    for i in app.tree.get_children():
        app.tree.delete(i)
    for i, (name, m) in enumerate(app.tasks):
        app.tree.insert("", "end", values=(name, m))