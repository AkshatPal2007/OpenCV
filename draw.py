import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1.paint with a color
# blank[:] = 0,0,255 
# cv.imshow('RED',blank)

#2.Draw a Rectangle
# cv.rectangle(blank,(0,0), (250,400), (0,255,255), thickness=-1)
# cv.imshow('Rectangle', blank)

#3. Draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# cv.imshow('circle', blank)

#4.Write text
cv.putText(blank, 'Hey', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)
cv.waitKey(0)