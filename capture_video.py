import numpy as np
import cv2
import time
import imutils

# The duration in seconds of the video captured
capture_duration = 3

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)
        # resize the frame
        #frame = imutils.resize(frame, width=480)
        out.write(frame)
        cv2.imshow('frame',frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()