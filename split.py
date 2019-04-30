    import cv2
    import os
    import numpy as np

    name  = input("Enter the classifier name\n")
    path = "images/"+name
    os.mkdir(path)
    print("Folder craeted for : ",name,"\n")

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

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
      pass
