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
        while lock:
            if latest_image is None:
                continue
            img = latest_image.copy() 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            mask = background_sub.apply(gray)
            _, thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 200:
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
    video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (320,240))

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
entry_z = tk.Entry(window,width=10).grid(row=0,column=1)

tk.Label(window, text="Координата X (м): ").grid(row=1, column=0, padx=20, pady=10)
entry_x=tk.Entry(window, width=10).grid(row=1, column=1)

tk.Label(window, text="Координата Y (м): ").grid(row=2, column=0, padx=20, pady=10)
entry_y = tk.Entry(window, width=10).grid(row=2, column=1)

tk.Label(window, text="Широта: ").grid(row=3, column=0, padx=20, pady=10)
entry_lat = tk.Entry(window, width=10).grid(row=3, column=1)

tk.Label(window, text="Долгота: ").grid(row=4, column=0, padx=20, pady=10)
entry_lon = tk.Entry(window, width=10).grid(row=4, column=1)

tk.Label(window, text="Скорость (м/с): ").grid(row=5, column=0, padx=20, pady=10)
entry_speed = tk.Entry(window, width=10).grid(row=5, column=1)

# Кнопки управления
takeoff_button = tk.Button(window, text="Взлет", width=20, bg="brown3", fg="white", relief="solid").grid(row=6,column=0,padx=20, pady=5)
land_button = tk.Button(window, text="Посадка", width=20, relief="solid").grid(row=7, column=0, padx=20,pady=5)
global_coordinates_button = tk.Button(window, text="Гл. Координаты", width=20, relief="solid").grid(row=8, column=0, padx=20, pady=5)
flip_button = tk.Button(window, text="Флип", width=20, relief="solid").grid(row=9, column=0, padx=20, pady=5)
load_plan_button = tk.Button(window, text="Загрузить план", width=20, relief="solid").grid(row=10, column=0, padx=20, pady=5)
home_button = tk.Button(window, text="Домой", width=20, relief="solid").grid(row=6, column=1, padx=20, pady=5)
telemetry_button = tk.Button(window, text="Телеметрия", width=20, relief="solid").grid(row=7, column=1, padx=20, pady=5)
local_coordinates = tk.Button(window, text="Лок. Координаты", width=20, relief="solid").grid(row=8, column=1, padx=20, pady=5)
activate_plan = tk.Button(window, text="Активировать план", width=20, relief="solid").grid(row=10, column=1, padx=20, pady=5 )

status_label = tk.Label(window, text="Состояние дрона", fg="blue")
status_label.grid(row=11, column=0, columnspan=2)
alt_label = tk.Label(window, text="Текущая высота", fg="blue")
alt_label.grid(row=10, column=3)

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
window.mainloop()
