import tkinter as tk
from tkinter import filedialog, messagebox
import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import json
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL import Image as PILImage, ImageTk
from datetime import datetime
import threading

rospy.init_node('fligth_control_gui')

bridge = CvBridge()
fullbody_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
background_sub = cv2.createBackgroundSubtractorMOG2()

latest_image = None
running_mode = None
lock = threading.Lock()
video_writer = None
flight_plan = None



get_telemetry = rospy.ServiceProxy("get_telemetry", srv.GetTelemetry)
navigate = rospy.ServiceProxy("navigate", srv.Navigate)
navigate_global = rospy.ServiceProxy("navigate_global", srv.NavigateGlobal)
land = rospy.ServiceProxy("land", Trigger)

start = get_telemetry()
home_possion = [start.lat, start.lon]
print(home_possion)
# Обновление высоты
def update_altitude():
    try:
        telem = get_telemetry()
        altitude = telem.z
        alt_label.config(text=f"Текущая высота {altitude:.2f} м")
    except:
        alt_label.config(text="Ошибка получения высоты")

    window.after(1000, update_altitude)

def arrival_wait(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id="navigate_target")
        if math.sqrt(telem.x**2 + telem.y**2 +telem.z**2 ) < tolerance:
            break
        rospy.sleep(0.2)

# Взлет
def takeoff():
    try:
        z = float(entry_z.get())
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = 1.0
        threading.Thread(target=navigate, args=(0, 0, z, speed, 1, "body", True)).start()
        status_label.config(text=f"Взлет на высоту {z} м со скоростью {speed} м/с")
        
    except:
        status_label.config(text="Ошибка: введите числовые значения для высоты и скорости")


# Посадка
def land_drone():
    threading.Thread(target=land).start()
    status_label.config(text="Дрон приземлился")

# Полет по локальным координатам
def fly_to_local_coodinates():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        if entry_z.get():
            z = float(entry_z.get())
        else:
            z = 0
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = 1.0
        threading.Thread(target=navigate, args=(x, y, z, speed, 1, "body", True)).start()
        status_label.config(text=f"X: {x}, Y: {y}, высотf {z} и скорость {speed}")
    except:
        status_label.config(text="Ошибка: введите числовые значения для  X, Y, высоты и скорости")

# Полет по глобальным координатам
def fly_to_global_coordinates():
    try:
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        if entry_z.get():
            z = float(entry_z.get())
        else:
            z = 3.0
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = 1.0
        threading.Thread(target=navigate_global, args=(lat, lon, z, speed, 1, "map", False)).start()
        status_label.config(text=f"Широта: {lat}, Долгота: {lon}")
    except:
        status_label.config(text="Ошибка: введите числовые значения для  широты, долготы, высоты и скорости")

#Возврат на начальную точку
def fly_home():
    if home_possion:
        if entry_z.get():
            z = float(entry_z.get())
        else:
            z = 3.0
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = 1.0
        lat, lon = home_possion[0], home_possion[1]
        threading.Thread(target=navigate_global, args=(lat, lon, z, speed, 1, "map", False)).start()
        status_label.config(text="Возвращаемся домой")
    else:
        status_label.config(text="Ошибка: точка взлета не определена")
        return

# Показ телеметрии
def show_telemetry():
    telem = get_telemetry()
    status_label.config(text=f"X = {telem.x}, Y = {telem.y}, Z = {telem.z}")


# Загрузка плана
def load_plan_file(filename):
    with open(filename, "r") as file:
        return json.load(file)

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Flight Plan Files", "*.plan")])
    if filename:
        if filename.endswith(".plan"):
            try:
                global flight_plan
                flight_plan = load_plan_file(filename)
                status_label.config(text=f"Файл плана полета {filename} успешно загружен")
            except:
                messagebox.showerror("Ошибка загрузки", f"Не удалось загрузить план полета {filename}")
        else:
            messagebox.showerror("Неверный файл", "Выберите файл с расширением .plan")

# Обработка и вывод изображения с камеры
def camera_image(msg):
    global latest_image
    with lock:
        latest_image = bridge.imgmsg_to_cv2(msg, 'bgr8')

image_sub = rospy.Subscriber('main_camera/image_raw', Image, camera_image, queue_size=1)

# Обновление изображения в Tkinter
def update_image():
    if latest_image is not None:
        with lock:
            img_rgb = cv2.cvtColor(latest_image, cv2.COLOR_BGR2RGB)
            img_pil = PILImage.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(image=img_pil)

            camera_label.config(image=img_tk)
            camera_label.image=img_tk
    window.after(100, update_image)

# Распознание объекта с каскадом
def detected_objects():
    global latest_image
    while running_mode == "objects":
        with lock:
            if latest_image is None:
                continue
            img = latest_image.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = fullbody_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=4, minSize=(30,30))

        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        display_image(img)

# Запуск режима распознания объектов с каскадом
def start_object_detection():
    stop_detection()
    global running_mode
    running_mode = "objects"
    threading.Thread(target=detected_objects, daemon=True).start()


# Остановка распознания
def stop_detection():
    global running_mode
    running_mode = None

# Распознание движущихся объектов
def detect_motion():
    global latest_image
    while running_mode == "motion":
        with lock:
            if latest_image is None:
                continue
            img = latest_image.copy()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = background_sub.apply(gray)
        _, thresh = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 400:
                cv2.polylines(img, [contour], isClosed=True, color=(0, 0, 255), thickness=1)
        display_image(img)

# Распознание объектов по цвету
def detect_by_color():
    global latest_image
    while running_mode == "color_detection":
        while lock:
            if latest_image is None:
                continue
            img = latest_image.copy()

        


# Запуск режима распознания по цветам
def start_detect_color():
    stop_detection()
    global running_mode
    running_mode = "color_detection"
    threading.Thread(target=detect_by_color, daemon=True).start()

# Заупуск режима распознавания движущихся объектов
def start_motion_detection():
    stop_detection()
    global running_mode
    running_mode = "motion"
    threading.Thread(target=detect_motion, daemon=True).start()


# Отображение видео
def display_image(img):
    global video_writer
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = PILImage.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    camera_label.config(image=img_tk)
    camera_label.image=img_tk

    if video_writer is not None:
        video_writer.write(img)

# Старт записи видео
def start_video_recording():
    global video_writer
    if video_writer is not None:
        messagebox.showinfo("Запись", "Видео уже записывается")
        return
    
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{time}.avi"
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (320, 240))

    def record():
        global latest_image
        while video_writer is not None:
            with lock:
                if latest_image is None:
                    continue
                video_writer.write(latest_image)
            rospy.sleep(0.03)
    threading.Thread(target=record, daemon=True).start()

# Остановка записи видео
def stop_video_recording():
    global video_writer
    if video_writer is not None:
        video_writer = None
        messagebox.showinfo("Запись", "Видео успешно сохранено")

# Окно
window = tk.Tk()
window.title("Управление дроном")
window.geometry("1080x550")

# Поля ввода и лейблы
tk.Label(window, text="Высота взлета (м): ").grid(row=0, column=0, padx=20, pady=10)
entry_z = tk.Entry(window,width=10)
entry_z.grid(row=0,column=1)

tk.Label(window, text="Координата X (м): ").grid(row=1, column=0, padx=20, pady=10)
entry_x = tk.Entry(window, width=10)
entry_x.grid(row=1, column=1)

tk.Label(window, text="Координата Y (м): ").grid(row=2, column=0, padx=20, pady=10)
entry_y = tk.Entry(window, width=10)
entry_y.grid(row=2, column=1)

tk.Label(window, text="Широта: ").grid(row=3, column=0, padx=20, pady=10)
entry_lat = tk.Entry(window, width=10)
entry_lat.grid(row=3, column=1)

tk.Label(window, text="Долгота: ").grid(row=4, column=0, padx=20, pady=10)
entry_lon = tk.Entry(window, width=10)
entry_lon.grid(row=4, column=1)

tk.Label(window, text="Скорость (м/с): ").grid(row=5, column=0, padx=20, pady=10)
entry_speed = tk.Entry(window, width=10)
entry_speed.grid(row=5, column=1)

# Кнопки управления
takeoff_button = tk.Button(window, text="Взлет", width=20, bg="brown3", fg="white", relief="solid", command=takeoff).grid(row=6,column=0,padx=20, pady=5)
land_button = tk.Button(window, text="Посадка", width=20, relief="solid", command=land).grid(row=7, column=0, padx=20,pady=5)
global_coordinates_button = tk.Button(window, text="Гл. Координаты", width=20, relief="solid",command=fly_to_global_coordinates).grid(row=8, column=0, padx=20, pady=5)
flip_button = tk.Button(window, text="Флип", width=20, relief="solid").grid(row=9, column=0, padx=20, pady=5)
load_plan_button = tk.Button(window, text="Загрузить план", width=20, relief="solid",command=browse_file).grid(row=10, column=0, padx=20, pady=5)
home_button = tk.Button(window, text="Домой", width=20, relief="solid", command=fly_home).grid(row=6, column=1, padx=20, pady=5)
telemetry_button = tk.Button(window, text="Телеметрия", width=20, relief="solid",command=show_telemetry).grid(row=7, column=1, padx=20, pady=5)
local_coordinates = tk.Button(window, text="Лок. Координаты", width=20, relief="solid",command=fly_to_local_coodinates).grid(row=8, column=1, padx=20, pady=5)
activate_plan = tk.Button(window, text="Активировать план", width=20, relief="solid").grid(row=10, column=1, padx=20, pady=5 )

status_label = tk.Label(window, text="Состояние дрона", fg="blue")
status_label.grid(row=11, column=0, columnspan=2)
alt_label = tk.Label(window, text="Текущая высота", fg="blue")
alt_label.grid(row=11, column=3, columnspan=2)

# Кнопки для камеры
detection_button = tk.Button(window, text="Распознать объект", width=20, bg="blue", fg="white", relief="solid",command=start_object_detection).grid(row=7, column=3, padx=20, pady=5)
detection_move_button = tk.Button(window, text="Распознать движение", width=20, bg="blue", fg="white", relief="solid", command=start_motion_detection).grid(row=8, column=3, padx=20, pady=5)
detection_color_button = tk.Button(window, text="Распознать цвета", width=20, bg="blue", fg="white", relief="solid", command=start_detect_color).grid(row=9, column=3, padx=20, pady=5)
stop_detection_button = tk.Button(window, text="Остановить", width=20, bg="red", fg="white", relief="solid",command=stop_detection).grid(row=10, column=3, padx=20, pady=5)
video_record_button = tk.Button(window, text="Записать видео", width=20, bg="green", fg="white", relief="solid", command=start_video_recording).grid(row=7, column=4, padx=20, pady=5)
stop_video_record_button = tk.Button(window, text="Остановить запись", width=20, bg="red", fg="white", relief="solid",command=stop_video_recording).grid(row=8, column=4, padx=20, pady=5)

camera_label = tk.Label(window)
camera_label.grid(row=0, column=3, rowspan=8)


window.after(100, update_image)
window.after(1000, update_altitude)
window.mainloop()
