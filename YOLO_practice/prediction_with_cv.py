from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('models/yolo11n.pt')

clases = open('models/clases.txt', 'r')

data = clases.read()

all_clases = data.split("\n")

detection_colors = []

for i in range(len(all_clases)):
    r = np.random.randint(0, 255)
    b = np.random.randint(0, 255)
    g = np.random.randint(0, 255)
    detection_colors.append((b, g, r))

frame = cv2.imread('src/3.jpg')

detection_params = model.predict(source=frame, conf=0.4, save=False)
dp = detection_params[0].numpy()
if len(dp) != 0:
    for i in range(len(detection_params[0])):
        boxes = detection_params[0].boxes
        box = boxes[i]
        clsId= box.cls.numpy()[0]
        conf = box.conf.numpy()[0]
        bb = box.xyxy.numpy()[0]
        
        cv2.rectangle(
            frame,
            (int(bb[0]), int(bb[1])),
            (int(bb[2]), int(bb[3])),
            detection_colors[int(clsId)],
            2
        )

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_size = 0.5
        cv2.putText(
            frame,
            all_clases[int(clsId)]+ ' ' + str(round(conf*100, 2)) + '%',
            (int(bb[0]+10), int(bb[1])+20),
            font,
            font_size,
            (255, 255,255),
            1,cv2.LINE_AA            
        )

    cv2.imshow("Objects Detection", frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()