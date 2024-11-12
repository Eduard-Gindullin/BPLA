from ultralytics import YOLO
import cv2

model = YOLO('models/yolo11n.pt')

image = 'src/2.jpg'

result = model.predict(source=image, show=True, conf=0.7, save=False)
cv2.waitKey(0)
cv2.destroyAllWindows()