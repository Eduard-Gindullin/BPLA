# Создание радиокнопки
import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
radiobutton = tk.Radiobutton(window, text="Выбрать", value=1)
radiobutton.pack(pady=40)

window.mainloop()
