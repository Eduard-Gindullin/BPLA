from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
window.geometry( "450x450")

image_path = "1.jpg"
image_pil  = Image.open(image_path)

#rotate
rotated_image_pil = image_pil.rotate(45)

#scale
scaled_image = image_pil.resize((image_pil.width // 4, image_pil.height //4))

rotated_image_tk = ImageTk.PhotoImage(rotated_image_pil)
scaled_image_tk = ImageTk.PhotoImage(scaled_image)

label = tk.Label(window, image= rotated_image_tk)
label = tk.Label(window, image= scaled_image_tk)
label.pack(padx=10, pady=10)

window.mainloop()