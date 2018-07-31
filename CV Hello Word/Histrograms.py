import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread("image.jpg")

histrogram=cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256]);plt.show()

