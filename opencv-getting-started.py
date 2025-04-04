import cv2

image = cv2.imread('field.png', 0)

window1 = cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow(window1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()


