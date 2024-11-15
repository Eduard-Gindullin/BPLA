# Создание выпадающего списка
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("450x450")
combo = ttk.Combobox(window, values=["Вариант 1", "Вариант 2", "Вариант 3"])
combo.pack(pady=40)

window.mainloop()
