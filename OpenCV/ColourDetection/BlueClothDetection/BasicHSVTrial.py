#Hue varies from 0-180 degree
#Sat varies form 0-255
#val varies form 0-255
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    HSV_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #blue mask
    low_blue = np.array([100, 100, 80]) #lower boundary
    high_blue = np.array([179, 255, 255]) #upper boundary
    blue_mask = cv2.inRange(HSV_Frame, low_blue, high_blue)
    blue_mask = cv2.medianBlur(blue_mask, 9) #bluring to reduce noice and get smooth image
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask) #frame&frame and will display only on while part of mask

    cv2.imshow("Frame", frame)
    cv2.imshow("HSV_Frame", HSV_Frame)
    cv2.imshow("Blue Mask", blue_mask)
    cv2.imshow("Blue", blue)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break

cv2.destroyAllWindows()
