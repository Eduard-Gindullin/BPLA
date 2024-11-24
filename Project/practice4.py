import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


planList = []


def add_end_point():
    lat = float(endEntry_lat.get())
    lon = float(endEntry_lon.get())
    z = float(endEntry_z.get())
    speed = float(endEntry_speed.get())
    currentPlan = (lat, lon, z, speed)
        
    if all([lat, lon, z, speed]):
        endEntry_lat.delete(0, 'end')
        endEntry_lon.delete(0, 'end')
        endEntry_z.delete(0, 'end')
        endEntry_speed.delete(0, 'end')
        global end_point
        end_point = currentPlan
        endLabel.config(text=f"Конечная точка полета: {end_point}")
        return end_point
    else:
        messagebox.showerror("Ошибка", "Все координаты должны быть введены") 

def add_starting_point():
    lat = float(startEntry_lat.get())
    lon = float(startEntry_lon.get())
    z = float(startEntry_z.get())
    speed = float(startEntry_speed.get())
    currentPlan = (lat, lon, z, speed)
        
    if all([lat, lon, z, speed]):
        startEntry_lat.delete(0, 'end')
        startEntry_lon.delete(0, 'end')
        startEntry_z.delete(0, 'end')
        startEntry_speed.delete(0, 'end')
        global starting_point
        starting_point = currentPlan
        startLabel.config(text=f"Начальная точка полета: {starting_point}")
        return starting_point 
    else:
        messagebox.showerror("Ошибка", "Все координаты должны быть введены")    



def updatePlanBox():
    plans.delete(0, tk.END)
    for i in planList:
        plans.insert(tk.END, i)


def add_mid_point():
    lat = float(midEntry_lat.get())
    lon = float(midEntry_lon.get())
    z = float(midEntry_z.get())
    speed = float(midEntry_speed.get())
    currentPlan = (lat, lon, z, speed)
        
    if all([lat, lon, z, speed]):
        midEntry_lat.delete(0, 'end')
        midEntry_lon.delete(0, 'end')
        midEntry_z.delete(0, 'end')
        midEntry_speed.delete(0, 'end')
        planList.append(currentPlan)
        updatePlanBox()
        return planList    
    else:
        messagebox.showerror("Ошибка", "Все координаты должны быть введены")


def delete_plan():
    selectPlan = plans.selection_get().split()
    selectPlan1 = tuple(map(float, selectPlan))
    if selectPlan is not None:
        if selectPlan1 in planList:
            planList.remove(selectPlan1)
            updatePlanBox()
        else:
            messagebox.showerror("Ошибка", "Элемент не найден в списке")

def delete_all_plans():
    answer = messagebox.askyesno("Подтвердите удаление", "Удалить все точки?")
    if answer:
        planList.clear()
        updatePlanBox()


def sort():
    planList.sort()
    updatePlanBox()


def sortReverse():
    planList.sort(reverse=True)
    updatePlanBox()


def calculate_flight_plan():
    planList.append(end_point)
    planList.insert(0, starting_point)

    # window1 = tk.Toplevel(window)
    # window1.title("Полет пройдет по следующим координатам")
    # window1.config(width=300, height=200)
    columns = ("lat", "lon", "z", "speed")
    window1 = ttk.Treeview(columns=columns, show="headings")
    window1.pack(fill=BOTH, expand=1)
    window1.heading("lat", text="Долгота")
    window1.heading("lon", text="Широта")
    window1.heading("z", text="Высота")
    window1.heading("speed", text="Скорость")

    for point in planList:
        window1.insert("", END, values=point)
    button_close = ttk.Button(
        window1,
        text="Вернутся",
        command=window1.destroy
    )
    button_close.place(x=700, y=900)

    button_close_all = ttk.Button(
        window1,
        text="Завершить",
        command=window.destroy
    )
    button_close_all.place(x=600, y=900)

    

    


window = tk.Tk()
window.geometry("800x1000")
window.title("Управление полетом")
window.resizable(False, False)


addButton = tk.Button(window, text="Добавить начальную точку", command=add_starting_point)
addButton.place(relx=0.01, rely=0.01, relwidth=0.35, relheight=0.1)

addButton = tk.Button(window, text="Добавить конечную точку", command=add_end_point)
addButton.place(relx=0.01, rely=0.15, relwidth=0.35, relheight=0.1)

addButton = tk.Button(window, text="Добавить промежуточную точку", command=add_mid_point)
addButton.place(relx=0.01, rely=0.29, relwidth=0.35, relheight=0.1)

delButton = tk.Button(window, text="Удалить", command=delete_plan)
delButton.place(relx=0.01, rely=0.4, relwidth=0.35, relheight=0.1)

delAllButton = tk.Button(window, text="Удалить все", command=delete_all_plans)
delAllButton.place(relx=0.01, rely=0.51, relwidth=0.35, relheight=0.1)

sortButton = tk.Button(window, text="Сортировать", command=sort)
sortButton.place(relx=0.01, rely=0.62, relwidth=0.35, relheight=0.1)

sortReverseButton = tk.Button(window, text="Обр. сортировка", command=sortReverse)
sortReverseButton.place(relx=0.01, rely=0.73, relwidth=0.35, relheight=0.1)

sortReverseButton = tk.Button(window, text="Построить маршрут", command=calculate_flight_plan)
sortReverseButton.place(relx=0.01, rely=0.84, relwidth=0.35, relheight=0.1)

startLabel = tk.Label(window, text="Введите координаты начальной точки полета")
startLabel.place(relx=0.4, rely=0.01)

startLabel_lat = tk.Label(window, text="Широта")
startLabel_lat.place(relx=0.4, rely=0.05)

startEntry_lat = tk.Entry(window)
startEntry_lat.place(relx=0.4, rely=0.07, relwidth=0.10)

startLabel_lon = tk.Label(window, text="Долгота")
startLabel_lon.place(relx=0.52, rely=0.05)

startEntry_lon = tk.Entry(window)
startEntry_lon.place(relx=0.52, rely=0.07, relwidth=0.10)

startLabel_z = tk.Label(window, text="Высота полета")
startLabel_z.place(relx=0.64, rely=0.05)

startEntry_z = tk.Entry(window)
startEntry_z.place(relx=0.64, rely=0.07, relwidth=0.10)

startLabel_speed = tk.Label(window, text="Скорость")
startLabel_speed.place(relx=0.80, rely=0.05)

startEntry_speed = tk.Entry(window)
startEntry_speed.place(relx=0.80, rely=0.07, relwidth=0.10)

startLabel = tk.Label(window, text="")
startLabel.place(relx=0.4, rely=0.1)


endLabel = tk.Label(window, text="Введите координаты конечной точки полета")
endLabel.place(relx=0.4, rely=0.15)

endLabel_lat = tk.Label(window, text="Широта")
endLabel_lat.place(relx=0.4, rely=0.19)

endEntry_lat = tk.Entry(window)
endEntry_lat.place(relx=0.4, rely=0.21, relwidth=0.10)

endLabel_lon = tk.Label(window, text="Долгота")
endLabel_lon.place(relx=0.52, rely=0.19)

endEntry_lon = tk.Entry(window)
endEntry_lon.place(relx=0.52, rely=0.21, relwidth=0.10)

endLabel_z = tk.Label(window, text="Высота полета")
endLabel_z.place(relx=0.64, rely=0.19)

endEntry_z = tk.Entry(window)
endEntry_z.place(relx=0.64, rely=0.21, relwidth=0.10)

endLabel_speed = tk.Label(window, text="Скорость")
endLabel_speed.place(relx=0.80, rely=0.19)

endEntry_speed = tk.Entry(window)
endEntry_speed.place(relx=0.80, rely=0.21, relwidth=0.10)

endLabel = tk.Label(window, text="")
endLabel.place(relx=0.4, rely=0.24)

midLabel = tk.Label(window, text="Введите координаты промежуточной точки полета")
midLabel.place(relx=0.4, rely=0.27)

midLabel_lat = tk.Label(window, text="Широта")
midLabel_lat.place(relx=0.4, rely=0.3)

midEntry_lat = tk.Entry(window)
midEntry_lat.place(relx=0.4, rely=0.33, relwidth=0.10)

midLabel_lon = tk.Label(window, text="Долгота")
midLabel_lon.place(relx=0.52, rely=0.3)

midEntry_lon = tk.Entry(window)
midEntry_lon.place(relx=0.52, rely=0.33, relwidth=0.10)

midLabel_z = tk.Label(window, text="Высота полета")
midLabel_z.place(relx=0.64, rely=0.3)

midEntry_z = tk.Entry(window)
midEntry_z.place(relx=0.64, rely=0.33, relwidth=0.10)

midLabel_speed = tk.Label(window, text="Скорость")
midLabel_speed.place(relx=0.80, rely=0.3)

midEntry_speed = tk.Entry(window)
midEntry_speed.place(relx=0.80, rely=0.33, relwidth=0.10)


plans = tk.Listbox(window)
plans.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.5)

window.mainloop()
