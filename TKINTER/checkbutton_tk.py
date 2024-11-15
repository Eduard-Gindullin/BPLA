# Создание чекбокса
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
checkbutton = tk.Checkbutton(window, text="Отметить")
checkbutton.pack(pady=30)

window.mainloop()