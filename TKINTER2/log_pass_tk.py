import tkinter as tk

def check():
    if password_entry.get() == "123456" and login_entry.get() == "user":
        info_label.config(text="Доступ разрешен", bg="green")
    elif password_entry.get() == "":
        info_label.config(text="Поле пароль пустое", bg="red")
    elif login_entry.get() == "":
        info_label.config(text="Поле логин пустое", bg="red")
    else:
        info_label.config(text="Неверные данные для входа", bg="red")

window = tk.Tk()
window.geometry("450x450")
window.title("Log/pass check")
window.resizable(False, False)

login_label = tk.Label(window, text="Введите Логин")
login_label.pack()
login_entry = tk.Entry(window)
login_entry.pack()

password_label = tk.Label(window, text="Введите Пароль")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()

info_label = tk.Label(window, text="")
info_label.pack()

check_button = tk.Button(window, text="Войти", command=check)
check_button.pack(side="bottom", pady=15)

window.mainloop()
