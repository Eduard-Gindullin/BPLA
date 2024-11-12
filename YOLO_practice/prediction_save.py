from ultralytics import YOLO
import cv2

model = YOLO('models/yolo11m.pt')

src = 'src/1.jpg'

save_dir = 'results'

result = model.predict(
    source=src, 
    show=True, 
    conf=0.4, 
    save=True, 
    project=save_dir
)

cv2.waitKey(0)
cv2.destroyAllWindows()
