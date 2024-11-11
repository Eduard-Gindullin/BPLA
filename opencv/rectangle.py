# Программа для рисования прямоугольника
import cv2

image = cv2.imread("1.jpeg")
cv2.rectangle(image, (150, 150), (300, 300), (0, 255, 0), 3)
cv2.imshow("Rectangle Image", image)
cv2.imwrite("Rectangle_image.jpeg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()