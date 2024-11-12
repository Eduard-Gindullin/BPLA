from ultralytics import YOLO
import cv2

model = YOLO("D:\Python projects\BPLA\YOLO_Train\best_worker.pt")
img = "D:\Python projects\BPLA\YOLO_Train\test\1.jpg"
print(model.names)
result = model.predict(source=img, show=True)
cv2.waitKey(0)
cv2.destroyAllWindows()