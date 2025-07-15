import cv2 as cv
import numpy as np

img = cv.imread('img/pfp.jpg')
cv.imshow('me', img)

blank= np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2-20, img.shape[0]//2-250), 150,255,-1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)