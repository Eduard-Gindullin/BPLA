# pip install numpy
# pip install opencv-python
# Программа для чтения изображения
import cv2

image = cv2.imread('1.jpeg')

cv2.imshow('Read Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()