# Получение данных с поля для ввода
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
entry = tk.Entry(window)
entry.pack(pady=20)

entry.insert(0, "Новое значение")

value = entry.get()
print(f"текущее значение \n{value}")

window.mainloop()
