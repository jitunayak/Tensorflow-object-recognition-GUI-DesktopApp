import eel
import os
import random
import cv2
import os
import numpy as np
import label_image

eel.init('web')                     

@eel.expose                         # Expose this function to Javascript
def handleinput(name):
    #name  = input("Enter the classifier name\n")
    path = "images/"+name
    if not os.path.isdir('images'):
        os.mkdir('images')
    try:
        os.mkdir(path)
        print("Folder created for : ",name,"\n")
    except:
        pass
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    eel.info("Press Q to stop taking pictures")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,1)
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    vidcap = cv2.VideoCapture('output.avi')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      if(success==True):
        cv2.imwrite('images/'+name+'/frame%d.jpg' % count, image)     # save frame as JPEG file
        print('Read a new frame: ', success)
        count += 1
      
    else:
      pass # Expose this function to Javascript

    eel.info("succesfully saved for  "+name)
    #os.system("rm output.avi")

@eel.expose
def detect_faces():
    print('detection started')
    eel.info("Press ESC to stop")
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

@eel.expose
def train_images():
    eel.info("Seat Back and wait.....")
    eel.mSpinner()
    try:
        os.system('python3 retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images')    
        eel.info("Training is completed")
        eel.mSpinner()
        eel.mAddTick()
    except:
        eel.info("connect to internet..")

eel.start('main2.html', size=(700, 400))


