import cv2
import numpy as np
import matplotlib

image=cv2.imread('image.jpg' )
#image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV )

b,g,r=cv2.split(image)

cv2.imshow("RGB",image)
cv2.imshow("R",r)
cv2.imshow("G",g)
cv2.imshow("B",b)

empty=np.zeros(image.shape[:2],dtype="uint8")

R=cv2.merge([empty,empty,r])
G=cv2.merge([empty,g,empty])
B=cv2.merge([b,empty,empty])


cv2.imshow("New R",R)
cv2.imshow("New G",G)
cv2.imshow("New B",B)


'''cv2.imshow("HSV",image)
cv2.imshow("H",image[:, :,0])
cv2.imshow("S",image[:, :,1])
cv2.imshow("V",image[:, :,2])'''

b,g,r=image[1,2]
#print b,g,r
#print image.shape

cv2.waitKey()
cv2.destroyAllWindows()