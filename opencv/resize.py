# Изменение размеров изображения
# 1000 x 800
import cv2

image = cv2.imread('output_image.jpeg')

width = int(input("Введите новую ширину: "))
height = int(input("Введите новую высоту: "))

resize_image = cv2.resize(image, (width, height))

cv2.imshow("Image", image)
cv2.imshow("Resize image", resize_image)
cv2.imwrite("ResizeImage.jpeg", resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()