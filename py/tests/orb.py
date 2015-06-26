#!/usr/bin/env python

'''
Test descriptors using ORB
'''
import cv2
import numpy as np

if __name__ == '__main__':

  orb = cv2.ORB_create()

  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()
  cv2.imshow('input', frame)
  print "Press ESC to exit"

  face = cv2.imread('data/face.png')
  cv2.imshow('face',face)
  kp = orb.detect(face,None)
  kp, des = orb.compute(face, kp)
  faced = cv2.drawKeypoints(face,kp,color=(0,255,0),outImage =face, flags=0)
  cv2.imshow('faced', faced)

  while(True):
    ret, frame = cap.read()

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

