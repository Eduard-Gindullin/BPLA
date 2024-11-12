from ultralytics import YOLO

model = YOLO('models/yolo11n.pt')

src = 'src/two_wheeler2.mp4'

target_class = 0

result = model.predict(source=src, conf=0.4, classes=[target_class], show=True, save=False)
