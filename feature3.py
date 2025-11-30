# feature3.py - Feature 3: Pause, Resume, +10 min, timer
import threading
import time
import tkinter.messagebox as mb

def setup(app):
    app.running = False
    app.paused = False

    btns = tk.Frame(app)
    btns.pack(pady=10)
    tk.Button(btns, text="Start", bg="green", fg="white", command=lambda: start(app)).grid(row=0,column=0,padx=8)
    tk.Button(btns, text="Pause", command=lambda: pause(app)).grid(row=0,column=1,padx=8)
    tk.Button(btns, text="Resume", command=lambda: resume(app)).grid(row=0,column=2,padx=8)
    tk.Button(btns, text="+10 min", bg="orange", command=lambda: add10(app)).grid(row=0,column=3,padx=8)

def start(app):
    if app.running or not app.tasks: return
    app.idx = 0
    app.remain = app.tasks[0][1] * 60
    app.running = True
    threading.Thread(target=countdown, args=(app,), daemon=True).start()

def countdown(app):
    while app.remain > 0 and app.running:
        if not app.paused:
            m, s = divmod(app.remain, 60)
            app.timer_label.config(text=f"{m:02d}:{s:02d}")
            app.name_label.config(text=app.tasks[app.idx][0])
            time.sleep(1)
            app.remain -= 1
        else:
            time.sleep(0.1)
    if app.remain <= 0:
        app.root.bell()
        next_task(app)

def pause(app):   app.paused = True
def resume(app):  app.paused = False
def add10(app):
    if app.running:
        app.remain += 600
        mb.showinfo("Extended", "+10 minutes added")

def next_task(app):
    if app.idx < len(app.tasks)-1:
        app.idx += 1
        app.remain = app.tasks[app.idx][1] * 60
    else:
        app.running = False
        app.timer_label.config(text="Finished")
