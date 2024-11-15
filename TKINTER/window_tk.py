# Создание окна
import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("400x500")
window.resizable(False, False)

window.mainloop()