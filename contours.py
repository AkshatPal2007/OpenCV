import cv2 as cv
import numpy as np

img = cv.imread('img/pfp.jpg')
cv.imshow('Me', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray) 

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur,125,15)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('th', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!') 

cv.drawContours(blank, contours, -1,(0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)