from SimpleCV import Camera, Display
from time import sleep
import serial
import time

myCamera = Camera(prop_set={'width': 320, 'height': 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
    frame = myCamera.getImage()
    faces = frame.findHaarFeatures('face')
    if faces:
    	for face in faces:
                print"Face at: " + str(face.coordinates())
                ser = serial.Serial('/dev/ttyACM0', 9600)
                time.sleep(2)
                ser.write(b'A')
                time.sleep(6)
                ser.close()

    else:
        print "No faces detected."
        ser = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)
        ser.write(b'B')
    frame.save(myDisplay)
    sleep(.1)
