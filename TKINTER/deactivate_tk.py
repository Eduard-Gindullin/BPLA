# Деактивация виджета
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
button = tk.Button(window, text="Кнопка")
button.pack(pady=40)

button.config(state="disabled")

window.mainloop()