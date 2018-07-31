import cv2
import numpy as np

img=cv2.imread('image.jpg')
#img=cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
#print +img.shape
B,G,R=img[10,20]
#print +B,G,R
#cv2.imwrite('out.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

