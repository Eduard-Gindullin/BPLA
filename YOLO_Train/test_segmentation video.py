from ultralytics import YOLO
import cv2

model = YOLO("best_ducks.pt")
print(model.names)
cap = cv2.VideoCapture("test/ducks.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model(frame)
    annotation = result[0].plot()
    cv2.imshow("Camera", annotation)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
