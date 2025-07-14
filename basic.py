import cv2 as cv

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

#Convert to Grey
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img , (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny',canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations= 1)
cv.imshow('Eroded', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropper', cropped)

cv.waitKey(0)