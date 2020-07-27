#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
imagefolder = '/home/pi/Documents/videos/'
format = '.h264'



def video():
   camera = PiCamera()
   camera.resolution = (1920, 1080)
   camera.framerate = 22
   camera.start_preview()
   time.sleep(2)
   camera.start_recording((imagefolder + 'video' + timestr + format), format='h264', quality=5)
   camera.wait_recording(30)
   camera.stop_recording()
   return;

video()


