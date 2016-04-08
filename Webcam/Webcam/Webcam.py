import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret,img = cap.read()

    # Operations on the captured frame
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image',gray)
    cv2.imshow('Normal image',img)
    if cv2.waitKey(0):
        break


cap.release()
cv2.destroyAllWindows()


