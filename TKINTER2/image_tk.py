from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
window.geometry("450x450")

image_path = "1.jpg"
image_pil = Image.open(image_path)

image_tk = ImageTk.PhotoImage(image_pil, (250, 250))

label = tk.Label(window, image=image_tk)
label.pack(padx=10, pady=10)

window.mainloop()
