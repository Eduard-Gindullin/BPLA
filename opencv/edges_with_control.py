# Определение края изображения с ползунками
import cv2

def nothing(x):
    pass

image = cv2.imread("1.jpeg")

cv2.namedWindow("Edges")

cv2.createTrackbar("Lower", "Edges", 0, 255, nothing)
cv2.createTrackbar("Upper", "Edges", 0, 255, nothing)

while True:

    lower_treshhold = cv2.getTrackbarPos("Lower", "Edges")
    upper_treshhold = cv2.getTrackbarPos("Upper", "Edges")

    edges = cv2.Canny(image, lower_treshhold, upper_treshhold)

    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.imwrite("Edges_Canny.jpeg", image)
cv2.destroyAllWindows()