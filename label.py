import cv2
import eel
import label_image
import os

@eel.expose
def detect():
    size = 4
    webcam = cv2.VideoCapture(0) 
    while True:
        (rval, im) = webcam.read()
        im=cv2.flip(im,1,0) 
        mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))
        cv2.imwrite('testimage.jpg',im)
        testimage = "testimage.jpg"
        text = label_image.main(testimage)
        text = text.title()
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(100,100), font, 2, (0,255,0), 2)
        cv2.imshow('Capture',   im)
        key = cv2.waitKey(10)
        if key == 27:
            break

detect()         