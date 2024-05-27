import cv2 as cv
import sys

img = cv.imread("/Users/parkermei/ImagingScience/baboon.png")
#cv.imshow("Display",img)
#k = cv.waitKey(0)

px = img[100,100]
print(px)