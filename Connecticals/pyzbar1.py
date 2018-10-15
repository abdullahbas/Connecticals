# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 01:52:31 2018

@author: trabz
"""









cam=cv2.VideoCapture(0)

while (True):
    ret,image_np = cam.read()
    cv2.imshow('image',cv2.resize(image_np,(800,600)))
    print(decode(image_np))
    if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          cam.release()
          break


