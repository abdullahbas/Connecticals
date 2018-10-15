# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:17:11 2018

@author: trabz
"""

import requests
import os
from pyzbar.pyzbar import decode
from PIL import Image
import cv2


barc=decode(Image.open('ind5.jpg'))
dat=barc[0][0].decode("utf-8")
cv2.imshow('im',cv2.imread('ind4.jpg'))
cv2.waitKey(2)
print(barc)


x=requests.get('http://m.barkodoku.com/'+dat)

indPro=x.text.find('Ürün')
indBarko=x.text.find('Menşei')


trimmed=x.text[indPro:indBarko]

substr=trimmed.split('>')

substr2=substr[1].split('<')

product=substr2[0]

from gtts import gTTS
tts = gTTS(text=product.lower(), lang='tr')


try:
    tts.save("goo121d.mp3")
    s="goo121d.mp3"
except:
    tts.save("goo122d.mp3")
    s="goo122d.mp3"



import pygame
pygame.mixer.init()
pygame.mixer.music.load(s)
pygame.mixer.music.play()
cv2.destroyAllWindows()
