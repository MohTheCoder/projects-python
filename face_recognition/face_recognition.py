__author__ = "Mohammad R."

import sys
import os

try:
    import numpy as np
except:
    input("you need to install numpy, do \"pip install numpy\" in terminal")
try:
    import cv2
except:
    input("you need to install numpy, do \"pip install opencv-python\" in terminal")

try:
    droppedFile = sys.argv[1]
except:
    droppedFile = input("Close and drag file into the .py, or just paste in the path of the file right now\n");
    
base = os.path.basename(str(droppedFile))
fileName = os.path.splitext(base)[0]
fileExtention = os.path.splitext(base)[1]

print(fileExtention)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(droppedFile)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputs/' + fileName + ' - OUTPUT_FACE_RECOGNITION' + fileExtention, -1, fps, (width,height))

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow('PRESS Q TO ESCAPE', frame)
        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
exit()



