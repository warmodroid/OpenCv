import numpy as np
import cv2


#Load image from folder


cv2.namedWindow('Rope',cv2.WINDOW_NORMAL)   #To resize the Window.
img = cv2.imread('i.jpg',1)

cv2.imshow('i',img)
k=cv2.waitKey(0)  #It waits indefinitely for a key stroke
if k ==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('new.jpg',img)
    cv2.destroyAllWindows()
