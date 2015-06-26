#!/usr/bin/env python

'''
Testing Adaptive Thresholding 
'''
import cv2

if __name__ == '__main__':

  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()

  cv2.imshow('input', frame)
  print "Press ESC to exit"

  while(True):

    ret, frame = cap.read()
    cv2.imshow('input', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray,5)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    cv2.imshow('binary',th1)
    cv2.imshow('adaptive_mean',th2)
    cv2.imshow('adaptive_gaussian',th3)

    option = cv2.waitKey(1)
    if option & 0xFF == 27:
        break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

