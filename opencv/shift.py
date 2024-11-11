# Программа для смещения изображения
import cv2
import numpy

image = cv2.imread("1.jpeg")

shift_x = int(input("Введите величину смещения по x: "))
shift_y = int(input("Введите величину смещения по y: "))

width = image.shape[1]
height = image.shape[0]

# Масштаб, поворот, свиг
# | 1 0 shift_x |
# | 0 1 shift_y |

shift_matrix = numpy.float32([[1, 0, shift_x],
                              [0, 1, shift_y]])

shifted_image = cv2.warpAffine(image, shift_matrix, (width, height))

cv2.imshow("Shifted Image", shifted_image)
cv2.imwrite("Shifted_image.jpeg", shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()