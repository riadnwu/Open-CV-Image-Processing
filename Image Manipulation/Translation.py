from itertools import imap

import cv2
import numpy

image=cv2.imread("image.jpg")

width,hight= image.shape[:2]

nw,nh=width/2,hight/5

d=numpy.float32([[1,0,nw],[0,1,nh]])
newImage=cv2.warpAffine(image,d,(width,hight))
cv2.imshow("Translation",newImage)
cv2.waitKey()
cv2.destroyAllWindows()