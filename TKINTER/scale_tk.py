# Создание ползунков
import tkinter as tk

window = tk.Tk()
window.geometry("350x350")
scale = tk.Scale(window, from_=0, to=100, orient="horizontal")
scale.pack(pady=30)

window.mainloop()
