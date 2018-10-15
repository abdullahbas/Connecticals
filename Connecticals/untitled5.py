# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 02:25:17 2018

@author: trabz
"""
import urllib
from urllib.request import urlopen
import cv2
import numpy as np
import time
 
# Replace the URL with your own IPwebcam shot.jpg IP:
porturl='http://192.168.1.21:8080/shot.jpg'
while True:
 
   imgResp=urllib.request.urlopen(porturl)
   imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
   img=cv2.imdecode(imgNp,-1)
 
   cv2.imshow('IPWebcam',img)
 
   if cv2.waitKey(10) & 0xFF == ord('q'):
      break