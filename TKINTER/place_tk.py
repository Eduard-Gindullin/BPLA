# Размещение place
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
label1 = tk.Label(window, text="Надпись 1")
label1.place(x=200, y=200)

label2 = tk.Label(window, text="Надпись 2")
label2.place(x=50, y=250)

window.mainloop()
