# Mycroft Face Recognition Voice Assistant
Automating an open source voice assistant to recognise faces and give personalised briefings. (Weather, News, etc.)
Demo: https://www.youtube.com/watch?v=KHHCviwfhes

# Hardware
* Raspberry Pi 3b ($35)
* PS3 Eye Camera ($7)
* Off-the-shelf speaker with a 3.5mm jack.

The easiest way to get started with Mycroft is to use the picroft image - https://mycroft.ai/get-started/
Using a pip installation of OpenCV, you can usually get most features you need without the full installation which takes to the tune of two hours - https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

For any sort of face recognition, there are usually three distinct phases - 
* Face Detection and Data gathering
* Training the Recogniser
* Face Recognition

MJRoBot does a better job of explaining #1 and #2 than I ever could - https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826

You might want to customise the names and indiviual briefings using
`nano face_recognition.py`
The comments should guide you through, provided you have a basic familiarity with python.

Once you have the trained model to recognise faces, run 
`python face_recognition.py`

Psst. You probably know this already, but if you're running the RPi using ssh, you might want to use 'screen' to open a terminal that keeps running even when the ssh connection is closed - https://linuxize.com/post/how-to-use-linux-screen/

# Acknowledgements
All software is built standing on the shoulders of giants. Thanks to-
* Mycroft developers and community - https://mycroft.ai/about-mycroft/
* MJRoBot's tutorial on face recognition using OpenCV - https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
* Adrian Rosebrock's tutorial on OpenCV installation using pip - https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/
