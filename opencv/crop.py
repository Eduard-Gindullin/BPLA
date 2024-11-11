# Программа для обрезки изображения
import cv2

image = cv2.imread("1.jpeg")

x = 200
y = 10
width = 500
height = 300

end_x = x + width
end_y = y + height

cropped_image = image[y:end_y, x:end_x]

cv2.imshow("Cropped Image", cropped_image)
cv2.imwrite("Cropped_Image.jpeg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()