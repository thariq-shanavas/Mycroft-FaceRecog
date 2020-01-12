''''
Real Time Face Recogition
    ==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
    ==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition and Marcelo Rovai - MJRoBot.org @ 21Feb18  
Developed by Thariq Shanavas
'''

import cv2
import numpy as np
import os
import time
import datetime

# This sets the cofidence threshold for recognising faces. 
#A lower threshold would result in fewer false positives, but also might miss people unless the camera captures the face very clearly.
confidence_threshold = 90

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#initiate id counter
id = 0

# names related to ids: example ==> Thariq: id=1,  etc
names = ['None', 'Thariq', 'Person 2']

# Initialize and start realtime video capture. 640 by 480 works for PSEye or the RPi camera
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widhth
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.05*cam.get(3)
minH = 0.05*cam.get(4)

# This makes sure each person is greeted only once in the morning or evening. Add more flags for more people
flag_Thariq_morning = 0
flag_Thariq_evening = 0

while True:

    now = datetime.datetime.now()
    t = now.hour
    # Morning briefing
    if (t>6 and t<12):
        ret, img =cam.read()
        #img = cv2.flip(img, -1) # In case your camera is flipped for some reason, uncomment this
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            #Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < confidence_threshold):
                id = names[id]
                print(id,' spotted at ',now.hour,':',now.minute,'on',now.month,'/',now.day)
                confidence = "  {0}%".format(round(100 - confidence))
                if (id == 'Thariq' and flag_Thariq_morning == 0):
                    os.system('mycroft-speak good morning terry, I hope you slept well')
                    #time.sleep(5)
                    os.system('mycroft-say-to Weather')
                    time.sleep(10)
                    os.system('mycroft-speak have a great day ahead')
                    flag_Thariq_morning = 1
                time.sleep(60)

            else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
    # evening briefing
    elif (t>14):

        ret, img =cam.read()
        #img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < confidence_threshold):
                id = names[id]
                print(id,' spotted at ',now.hour,':',now.minute,'on',now.month,'/',now.day)
                confidence = "  {0}%".format(round(100 - confidence))
                if (id == 'Thariq' and flag_Thariq_evening == 0):
                    os.system('mycroft-speak welcome home terry, I hope you had a wondeful day')
                    flag_Thariq_evening = 1
                time.sleep(60)

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

    else:
        time.sleep(120)
        flag_Thariq_morning = 0
        flag_Thariq_evening = 0
