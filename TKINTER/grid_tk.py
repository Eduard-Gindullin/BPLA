# Размещение по grid
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

label1 = tk.Label(window, text="Надпись 1")
# label1.pack(pady=30)
label1.grid(row=0, column=0, pady=20)

label2 = tk.Label(window, text="Надпись 2")
# label2.pack(pady=30)
label2.grid(row=0, column=1, pady=20)

label4 = tk.Label(window, text="Надпись 2")
# label2.pack(pady=30)
label4.grid(row=2, column=2, pady=20)

label5 = tk.Label(window, text="Надпись 2")
# label2.pack(pady=30)
label5.grid(row=3, column=3, pady=20)

label6 = tk.Label(window, text="Надпись 3")
# label2.pack(pady=30)
label6.grid(row=4, column=5, pady=20)

window.mainloop()