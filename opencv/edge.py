# Программа для выделения края изображения
import cv2

image = cv2.imread("1.jpeg")

edges_image = cv2.Canny(image, 100, 200)

cv2.imshow("Edges Image", edges_image)
cv2.imwrite("Edges_image.jpeg", edges_image)
cv2.waitKey(0)
cv2.destroyAllWindows()