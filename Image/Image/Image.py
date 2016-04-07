import numpy as np
import cv2


#Load image from folder

img = cv2.imread('i.jpg',0)
cv2.imshow('i',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
