import cv2
import numpy

image=cv2.imread("image.jpg")

reImage=cv2.resize(image,None,fx=.3,fy=.3)
cv2.imshow("Resize",reImage)
cv2.waitKey()

r1=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Inter Cubic",r1)
cv2.waitKey()