import cv2 as cv

img = cv.imread('img/pfp.jpg')
cv.imshow('Me', img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray,170,255, cv.THRESH_BINARY)
cv.imshow('simple thres', thresh)

#Simple Thresholding Inverse
threshold, thresh_inv = cv.threshold(gray,170,255, cv.THRESH_BINARY_INV)
cv.imshow('simple thres inverse', thresh_inv)

#Adaptive Thresh
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('Adaptive Thresh', adaptive_thresh)

cv.waitKey(0)