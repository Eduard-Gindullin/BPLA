# https://roboflow.com/
# https://www.kaggle.com/datasets
# https://universe.roboflow.com/alshayn/ducks-jy9v0/dataset/1
# https://disk.yandex.ru/d/IOR7xWeqd1qbhA 
# https://colab.research.google.com/drive/1cP6diWpAThONR53Ogta_DSv2oT4ac5WM?usp=sharing

from ultralytics import YOLO
import os

model = YOLO("yolo11n-seg.pt")

save_dir = os.path.join(os.getcwd(), "YOLO_train_results")

result = model.train(
    data="Ducks.v1i.yolov11/data.yaml",
    epochs=10,
    imgsz=300,
    plots=True,
    project=save_dir,
    name="train"
)
