import cv2 as cv

# img = cv.imread('img/cat.jpg')

# cv.imshow('Cat', img)

##Read video
capture = cv.VideoCapture('vid/scene.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()