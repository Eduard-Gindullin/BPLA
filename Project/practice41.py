import tkinter as tk
from tkinter import filedialog, messagebox
import rospy
from clover import srv
from std_srvs.srv import Trigger
import numpy as np

# Создание выпадающего списка
import tkinter as tk
from tkinter import ttk

flight_position = []
flight_position.append((1,2,3,4))
flight_position.append((6,7,8,9))
flight_position.insert(0, (10, 11, 12, 13))
flight_position.insert(0, (14, 15, 16, 17))
print(flight_position)

flight_plan = []


def updateListBox():
    tasks.delete(0, tk.END)
    for i in flight_plan:
        flight_plan.insert(tk.END, i)


def add_task():
    currentTask = float(taskEntry.get())
    if currentTask != "":
        taskEntry.delete(0, tk.END)
        flight_plan.append(currentTask)
        updateListBox()
    else:
        messagebox.showerror("Ошибка", "Поле пустое")


def delete_task():
    selectTask = tasks.selection_get()
    flight_plan.remove(selectTask)
    updateListBox()


def delete_all_tasks():
    answer = messagebox.askyesno("Подтвердите удаление", "Удалить все задачи?")
    if answer:
        flight_plan.clear()
        updateListBox()


def sort():
    flight_plan.sort()
    updateListBox()


def sortReverse():
    flight_plan.sort(reverse=True)
    updateListBox()


window = tk.Tk()
window.geometry("800x650")
window.title("ToDo")
window.resizable(False, False)

addButton = tk.Button(window, text="Добавить", command=add_task)
addButton.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.1)

delButton = tk.Button(window, text="Удалить", command=delete_task)
delButton.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.1)

delAllButton = tk.Button(window, text="Удалить все", command=delete_all_tasks)
delAllButton.place(relx=0.05, rely=0.3, relwidth=0.3, relheight=0.1)

sortButton = tk.Button(window, text="Сортировать", command=sort)
sortButton.place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.1)

sortReverseButton = tk.Button(window, text="Обр. сортировка", command=sortReverse)
sortReverseButton.place(relx=0.05, rely=0.5, relwidth=0.3, relheight=0.1)

enterLabel = tk.Label(window, text="Введите задачу")
enterLabel.place(relx=0.4, rely=0.1)

taskEntry = tk.Entry(window)
taskEntry.place(relx=0.4, rely=0.15, relwidth=0.55)

tasks = tk.Listbox(window)
tasks.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.6)



window = tk.Tk()
window.geometry("450x450")
combo = ttk.Combobox(window, values=flight_position)
combo.pack(pady=40)

window.mainloop()