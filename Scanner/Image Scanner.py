import cv2
import numpy as np

image=cv2.imread("2.jpg",0)
image=cv2.GaussianBlur(image,(3,3),0)
#cv2.imshow("Original",image)

theresh=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)


#_,os=cv2.transpose(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Scanne",theresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
