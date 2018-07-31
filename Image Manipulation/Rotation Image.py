import cv2
import numpy

image=cv2.imread("image.jpg")
h,w=image.shape[:2]
rotation=cv2.getRotationMatrix2D((w/2,h/2),-180,.7)
newImage=cv2.warpAffine(image,rotation,(w,h))

cv2.imshow("Rotation",newImage)

#newRotat=cv2.transpose(image,180)
#cv2.imshow("other",newRotat)
cv2.waitKey()
cv2.destroyAllWindows()