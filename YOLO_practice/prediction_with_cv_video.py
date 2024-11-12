import cv2
from ultralytics import YOLO
import numpy as np

clases = open("models/clases.txt")
data = clases.read()
all_classes = data.split('\n')

detection_colors = []
for i in range(len(all_classes)):
    r = np.random.randint(0, 255)
    b = np.random.randint(0, 255)
    g = np.random.randint(0, 255)
    detection_colors.append((b, g, r))

model = YOLO("models/yolo11n.pt")

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture("src/1.mp4")

while True:
    ret = cap.read()
    if ret[0]:
        frame = ret[1]
    else:
        break

    detect_params = model.predict(source=[frame], conf=0.25)

    dp = detect_params[0].numpy()

    if len(dp) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]
            clsId = box.cls.numpy()[0]
            bb = box.xyxy.numpy()[0]
            conf = box.conf.numpy()[0]
            
            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsId)],
                2
            )

            cv2.putText(
                frame,
                all_classes[int(clsId)] + " " + str(round(conf*100,2))+ "%",
                (int(bb[0])+10, int(bb[1])-10),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.7,
                (0, 255, 255),
                1,
                cv2.LINE_AA                
            )
    cv2.imshow("Detection Video", frame)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()