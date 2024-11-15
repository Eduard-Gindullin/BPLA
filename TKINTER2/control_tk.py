import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import tkinter as tk

# Инициализация ROS
rospy.init_node('flight_control_gui')
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

# Функция ожидания прибытия до целевой точки
def arrival_wait(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

# Взлет
def takeoff():
    try:
        z = float(entry_height.get())
        navigate(x=0, y=0, z=z, frame_id='body', auto_arm=True)
        arrival_wait()
        home_position[0] = start.lat
        home_position[1] = start.lon
        status_label.config(text=f"Коптер взлетел на высоту {z} м")
    except ValueError:
        status_label.config(text="Ошибка: введите числовое значение для высоты")

# Посадка
def land_drone():
    land()
    status_label.config(text="Дрон приземлился")

# Полет по локальным координатам
def fly_to_local_coordinates():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        navigate(x=x, y=y, z=0, frame_id='body', yaw=math.inf, speed=1)
        arrival_wait()
        status_label.config(text=f"Дрон достиг точки X: {x}, Y: {y}")
    except ValueError:
        status_label.config(text="Ошибка: введите числовые значения для X и Y")

# Полет по глобальным координатам
def fly_to_global_coordinates():
    try:
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        navigate_global(lat=lat, lon=lon, z=3, yaw=math.inf, speed=1)
        arrival_wait()
        status_label.config(text=f"Дрон достиг точки широта: {lat}, долгота: {lon}")
    except ValueError:
        status_label.config(text="Ошибка: введите числовые значения для широты и долготы")

# Возврат домой
def fly_home():
    if home_position[0] is None or home_position[1] is None:
        status_label.config(text="Ошибка: точка взлета не определена")
        return
    navigate_global(lat=home_position[0], lon=home_position[1], z=3, yaw=math.inf, speed=1)
    arrival_wait()
    status_label.config(text="Возвращаемся домой")

# Получение текущей телеметрии
def show_telemetry():
    telem = get_telemetry()
    status_label.config(text=f"Телеметрия: x={telem.x}, y={telem.y}, z={telem.z}")

# Создание окна Tkinter
window = tk.Tk()
window.title("Управление дроном")

home_position = [None, None]
start = get_telemetry()

# Поля ввода
tk.Label(window, text="Высота взлета (м):").grid(row=0, column=0)
entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1)

tk.Label(window, text="Координата X (м):").grid(row=1, column=0)
entry_x = tk.Entry(window)
entry_x.grid(row=1, column=1)

tk.Label(window, text="Координата Y (м):").grid(row=2, column=0)
entry_y = tk.Entry(window)
entry_y.grid(row=2, column=1)

tk.Label(window, text="Широта:").grid(row=3, column=0)
entry_lat = tk.Entry(window)
entry_lat.grid(row=3, column=1)

tk.Label(window, text="Долгота:").grid(row=4, column=0)
entry_lon = tk.Entry(window)
entry_lon.grid(row=4, column=1)

# Кнопки управления
tk.Button(window, text="Взлет", command=takeoff).grid(row=5, column=0)
tk.Button(window, text="Полет по локальным координатам", command=fly_to_local_coordinates).grid(row=5, column=1)
tk.Button(window, text="Полет по глобальным координатам", command=fly_to_global_coordinates).grid(row=6, column=0)
tk.Button(window, text="Вернуться домой", command=fly_home).grid(row=6, column=1)
tk.Button(window, text="Посадка", command=land_drone).grid(row=7, column=0)
tk.Button(window, text="Текущая телеметрия", command=show_telemetry).grid(row=7, column=1)

# Метка для отображения статуса
status_label = tk.Label(window, text="Состояние дрона", fg="blue")
status_label.grid(row=8, column=0, columnspan=2)

# Запуск главного цикла Tkinter
window.mainloop()