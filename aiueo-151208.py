import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    img = cv2.medianBlur(frame,5)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,250,
                        param1=50,param2=30,minRadius=0,maxRadius=0)

    if circles is None:
        cv2.imshow('frame',cimg)
        continue
    print circles
    #circles = np.uint16(np.around(circles))
    
    for i in circles[0,:]:
       # draw the outer circle
       cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
       # draw the center of the circle
       cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    #Display the resulting frame
    cv2.imshow('frame',cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

