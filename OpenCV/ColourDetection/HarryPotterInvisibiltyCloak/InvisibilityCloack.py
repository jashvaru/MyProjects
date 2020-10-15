import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(30):
    ret, background = cap.read()

background = cv2.flip(background,1)

while True:
    #capturing the live frame
    ret, img = cap.read()
    img = cv2.flip(img, 1) #flipping the img over xaxis

    #coverting each frame from BGR to HSV color space
    HSV_Frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #range
    lower_blue = np.array([90, 100,100])
    upper_blue = np.array([179,255,255])
    mask1 = cv2.inRange(HSV_Frame, lower_blue, upper_blue)

    #To reduce the noise in the img
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    #creating a mask to display only blue cloth over black background
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    #Taking the still background image and showing part of img where mask is present
    res2 = cv2.bitwise_and(background, background, mask=mask1)
    #overlaping the two imgs
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Mask1", mask1) #blue cloth will shown as white pixel over black background
    cv2.imshow("Result1", res1)
    cv2.imshow("Result2", res2)
    cv2.imshow("final_output", final_output)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break

cv2.destroyAllWindows()

