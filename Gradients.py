import cv2 as cv
import numpy as np

img = cv.imread('img/cat.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sabel
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('combined', combined)

canny = cv.Canny(gray, 150,175)
cv.imshow('canny', canny)

cv.waitKey(0)
