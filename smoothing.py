import cv2 as cv

img = cv.imread('img/pfp.jpg')
cv.imshow('me', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Avg blur', average)

#GaussianBlur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)