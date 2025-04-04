import cv2

image = cv2.imread('field.png', 0)

print("Image shape:", image.shape)
print("Image size:", image.size)

window1 = cv2.namedWindow('image', cv2.WINDOW_NORMAL)

alive = True

print("Press 'q' to quit the window")

while alive:
  cv2.imshow(window1, image)
  keypress = cv2.waitKey(1)
  if keypress == ord('q'):
    alive = False

cv2.destroyAllWindows()


