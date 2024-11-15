# Создание поля для ввода
import tkinter as tk

window = tk.Tk()
window.geometry("450x450")
entry = tk.Entry(window, width=20)
entry.pack(pady=50)

window.mainloop()
