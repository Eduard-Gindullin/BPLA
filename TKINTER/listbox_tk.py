# Создание списка
import tkinter as tk

window = tk.Tk()
window.geometry("350x350")
listbox = tk.Listbox(window)
listbox.pack(pady=30)

for item in ["Элемент 1", "Элемент 2", "Элемент 3"]:
    listbox.insert(tk.END, item)

window.mainloop()
