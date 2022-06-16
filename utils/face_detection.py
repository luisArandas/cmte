

# fd

import cv2
import dearpygui.dearpygui as dpg
cv2.namedWindow("face detection")

vc = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

rval, frame = vc.read()

while True:

   if frame is not None:
      cv2.imshow("face detection", frame)

   rval, frame = vc.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)
   # compute this one for it to be more accurate
   # resized = cv2.resize(frame, (150,150), interpolation = cv2.INTER_AREA)

   for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break