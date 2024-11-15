# Стили элементов 1
# import tkinter as tk

# window = tk.Tk()
# window.geometry("400x400")
# window.config(background="red")

# button = tk.Button(window, text="press")
# button.pack(pady=30)
# button.config(borderwidth=0, background="blue")

# window.mainloop()

# Стили элементов 2
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")
window.style = ttk.Style()
window.style.theme_use("aqua")

window.mainloop()