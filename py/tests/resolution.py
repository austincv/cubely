#!/usr/bin/env python

'''
increases the video frame size by increments
of 10 and checks the frame for actual size and 
prints every new size of frame found

'''
import cv2

if __name__ == '__main__':

  cap = cv2.VideoCapture(0)
  i = 100 # starting point
  wo = 480
  ho = 640

  while(True):

    cap.set(3,i)
    cap.set(4,i)
    i=i+10
    ret, frame = cap.read()
    w = len(frame)
    h = len(frame[0])
    if w != wo:
      print w,h
      wo = w
      ho = h
    if i > 2000:
        break

  # When everything done, release the capture
  cap.release()

