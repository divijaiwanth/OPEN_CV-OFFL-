#arthametic operation
import cv2 as cv 

img1 = ''
img2 = ''
cv.add(img1,img2)  # syntax cv.add(img1,img2,...) or img[:,:,0] ((rows , colums , channels))


#added weighted fuction(transparency)
cv.addWeighted(img1,0.3,img2,0.7,0)  #synatx cv.addWeighted(img,weight_of_img,img2,weight_of_img,0)