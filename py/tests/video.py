#!/usr/bin/env python

'''
Test if video from webcam is working
Double click on the video to change resolution

'''
import cv2


clicked = True
i = 0 #defaults to 640,480

res =[(160,120),(240,160),(320,240),(400,240),(480,320),(640,480),(768,480),(854,480),(800,600),(960,640),(1024,576),(1024,600),(1024,768),(1280,1024),(1920,1080)]


def next(event,x,y,flags,param):
  global clicked,i
  if event == cv2.EVENT_LBUTTONDBLCLK:
    clicked = True
    i=i+1 if i<len(res)-2 else 0



if __name__ == '__main__':

  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()

  cv2.imshow('input', frame)
  cv2.setMouseCallback('input',next)
  print "Press ESC to exit"
  while(True):

    if clicked:
        clicked = False
        x,y = res[i]
        print res[i]
        cap.set(3,x)
        cap.set(4,y)

    ret, frame = cap.read()
    cv2.imshow('input', frame)
    option = cv2.waitKey(1)
    if option & 0xFF == 27:
        break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

