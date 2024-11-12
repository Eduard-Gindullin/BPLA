# https://roboflow.com/
# https://www.kaggle.com/datasets
# https://disk.yandex.ru/d/pudemuYnmtpXVA
# https://disk.yandex.ru/d/mh_1RXuA1QlL9w
# https://colab.research.google.com/drive/1GPxnFx_EN0p6Tyxkx0OrYysFGjnjB89x?usp=sharing

from ultralytics import YOLO
import os

model = YOLO("D:\Python projects\BPLA\YOLO_Train\yolo11n.pt")

save_dir = os.path.join(os.getcwd(), "YOLO_train_results")

result = model.train(
    data="D:\Python projects\BPLA\YOLO_Train\Workers.v1i.yolov11\data.yaml",
    epochs=50,
    imgsz=300,
    patience=20,
    plots=True,
    project=save_dir,
    name="train"
)
