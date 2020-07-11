#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
imagefolder = '/home/pi/Documents/images/'
format = '.jpg'

def image():
   camera = PiCamera()
   camera.resolution = (1920, 1080)
   camera.start_preview()
   sleep(2)
   camera.capture(imagefolder + 'image' + timestr + format)
   return;

image()

#cmd = "raspstill -vf -o /home/pi/Documents/images/image.jpeg"
