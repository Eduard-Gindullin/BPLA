# Программа для создания надписи на изображении
import cv2

image = cv2.imread("1.jpeg")

font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello World"
cv2.putText(image, text, (150, 150), font, 3, (0, 0, 0), 4, cv2.LINE_AA)

cv2.imshow("Image with text", image)
cv2.imwrite("Image_with_text.jpeg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()