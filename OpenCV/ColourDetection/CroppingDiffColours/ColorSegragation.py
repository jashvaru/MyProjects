import cv2
import numpy as np

img = cv2.imread('Color&Shapes.jpg')
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#hsv range for blue
lower_blue = np.array([80,100,100])
upper_blue = np.array([130, 255, 255])

#hsv range for yellow
lower_yellow = np.array([25,100,100])
upper_yellow = np.array([40, 255, 255])

#Finding contours from the mask and saving the img
Bmask = cv2.inRange(HSV, lower_blue, upper_blue)
contours, hierarchy = cv2.findContours(Bmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
x,y,w,h = cv2.boundingRect(contours[0])
shape1 = img[y:y+h, x:x+w]
cv2.imwrite("Blue.jpg", shape1)

Ymask = cv2.inRange(HSV, lower_yellow, upper_yellow)
contours, hierarchy = cv2.findContours(Ymask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
x,y,w,h = cv2.boundingRect(contours[0])
shape2 = img[y:y+h, x:x+w]
cv2.imwrite("yellow.jpg", shape2)


cv2.imshow("OG img", img)
cv2.imshow("Blue mask", Bmask)
cv2.imshow("Yellow mask", Ymask)
cv2.imshow("Shape1", shape1)
cv2.imshow("Shape2", shape2)
key = cv2.waitKey()
if key == ord('s'):
    cv2.destroyAllWindows()


