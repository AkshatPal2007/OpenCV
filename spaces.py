import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/cat.jpg')
cv.imshow('Cat',img)


#BGR to Grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# #BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# #BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)

#grey to BGR

g2b = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('g2b', g2b)


# plt.imshow(img)
# plt.show()



cv.waitKey(0)