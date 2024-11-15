# Создание кнопки
import tkinter as tk

window = tk.Tk()
window.geometry("250x250")
button = tk.Button(window, text="Нажми меня")
button.pack(padx=80, pady=80)

window.mainloop()