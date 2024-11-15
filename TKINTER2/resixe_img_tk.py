import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("450x450")

image_path = "D:\\Python projects\\TKINTER2\\src\\1.jpg"
image_pil = Image.open(image_path)

# rotate
rotated_image_pil = image_pil.rotate(45)
rotated_image_tk = ImageTk.PhotoImage(rotated_image_pil, (250, 250))



label = tk.Label(window, image=rotated_image_tk)
label.pack(padx=10, pady=10)


window.mainloop()