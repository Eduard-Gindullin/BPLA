# Поворот изображения
import cv2

image = cv2.imread("1.jpeg")

angle = int(input("Введите угол поворота: "))

width = image.shape[1]
height = image.shape[0]

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center = center, angle = angle, scale = 1.0)
rotate_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotate_image)
cv2.imwrite('Rotated_image.jpeg', rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()