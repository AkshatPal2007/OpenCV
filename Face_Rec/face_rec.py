import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('Face_Rec_1/haar_face.xml')

people = ['Akshat', 'mummy']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Face_Rec/face_trained.yml')

img = cv.imread(r'C:\Users\Akshat\Pictures\photo.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the face
faces_rect = haar_cascade.detectMultiScale(gray,1.1,8)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label ={people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0,(0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)