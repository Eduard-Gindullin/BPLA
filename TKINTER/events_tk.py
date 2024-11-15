import tkinter as tk

def click(event):
    print(f"кнопка нажата в {event.x}, {event.y}")

window = tk.Tk()
window.geometry('400x400')

window.bind("<Button-1>",click)

window.mainloop()