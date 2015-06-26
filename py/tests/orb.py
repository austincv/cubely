#!/usr/bin/env python

'''
Test descriptors using ORB
'''
import cv2
import numpy as np

if __name__ == '__main__':
  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()
  cv2.imshow('input', frame)
  print "Press ESC to exit"

  while(True):
    ret, frame = cap.read()

    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(frame,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(frame, kp)

    # draw only keypoints location,not size and orientation
    framed = cv2.drawKeypoints(frame,kp,color=(0,255,0),outImage =frame, flags=0)

    cv2.imshow('input', framed)
    option = cv2.waitKey(1)

    if option & 0xFF == 27:
        break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

