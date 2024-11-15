import tkinter as tk


def copy_text():
    selected_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    window.clipboard_clear()
    window.clipboard_append(selected_text)


window = tk.Tk()
window.geometry("450x450")

text = tk.Text(window, wrap="word", width=30, height=5)
text.pack(padx=10, pady=10)

text.insert("1.0", "Этот текст можно выделить скопировать")

copy_button = tk.Button(window, text="Копировать", command=copy_text)
copy_button.pack(padx=10, pady=10)

window.mainloop()
