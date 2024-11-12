from ultralytics import YOLO
import cv2

model = YOLO('models/yolo11n.pt')

save_path = 'results/ouput_video.avi'

cap = cv2.VideoCapture('src/pedestrians.avi')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(save_path,fourcc, fps, (width, height))

while True:
    ret = cap.read()
    if ret[0]:
        frame = ret[1]
    else:
        break

    results = model.predict(frame, conf=0.5)
    print(results)
    annotated_frame = results[0].plot()
    cv2.imshow("Detections", annotated_frame)

    out.write(annotated_frame)

    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()