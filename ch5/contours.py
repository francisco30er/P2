import cv2
import numpy as np
import sys
import os.path

blue, green, red = cv2.split(img)
blue_edges = cv2.Canny(blue, 200, 250)
green_edges = cv2.Canny(green, 200, 250)
red_edges = cv2.Canny(red, 200, 250)

edges = blue_edges | green_edges | red_edges


new_image = edges.copy()
new_image.fill(255)

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        color = np.random.randint(0,255,(3)).tolist()  # Select a random color
        cv2.drawContours(drawing,[cnt],0,color,2)
######################################################
	new_image = cv2.blur(new_image, (2, 2))
	cv2.imwrite(output_file, new_image)
###################################################
        cv2.imshow('output',drawing)
	
    cv2.imshow('input',img)

img = cv2.imread('plate.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

cv2.namedWindow('input',cv2.WINDOW_AUTOSIZE)

thresh = 100
max_thresh = 255

cv2.createTrackbar('canny thresh:','input',thresh,max_thresh,thresh_callback)

thresh_callback(thresh)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
