from ultralytics import YOLO
import cv2

model = YOLO("best_ducks.pt")

source = "test/1.jpg"

result = model.predict(source=source, show=True, conf=0.4)

cv2.waitKey(0)
cv2.destroyAllWindows()
