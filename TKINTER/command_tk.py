# События
import tkinter as tk

def click_button():
    print("Кнопка нажата")

window = tk.Tk()
window.geometry("400x400")
button = tk.Button(window, text="Кнопка",command=click_button)
button.pack(pady=30)

window.mainloop()