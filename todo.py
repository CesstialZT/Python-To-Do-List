from tkinter import *
from tkinter import messagebox

# Functions
def newTask():
    task = " • " + my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter a task.")

def deleteTask():
    lb.delete(ANCHOR)

# Configurations   
ws = Tk()
ws.geometry('300x500+500+200')
ws.title('My To Do List')
ws.config(bg='#D4E09B')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

# Elements
lb = Listbox(
    frame,
    width=22,
    height=15,
    font=('Montserrat', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='#D4E09B',
    activestyle="none",
    bg='#F6F4D2'
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [' • Create a new task!']

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Montserrat', 24),
    bg='#F6F4D2'
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Montserrat'),
    bg='#F6F4D2',
    padx=20,
    pady=10,
    command=newTask,
)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Montserrat'),
    bg='#F6F4D2',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()