# Создание многострочных текстовых полей
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
text = tk.Text(window, width=30, height=5)
text.pack(pady=40)

window.mainloop()