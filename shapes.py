import cv2 as cv 
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# pts = np.array([[10,100],[100,50],[200,100],[250,200]], np.int32)
# # pts = pts.reshape((-1,1,2))
# cv.polylines(img,[pts],True,(0,255,255))


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'DJxSTAR',(1,450), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow('img',img)

cv.waitKey(0)