#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import time




def video():
   camera = PiCamera()
   camera.resolution = (1920, 1080)
   camera.framerate = 25
   camera.start_preview()
   time.sleep(2)
   camera.start_recording('my_video.h264', format='h264', quality=5)
   camera.wait_recording(30)
   camera.stop_recording()
   return;

video()


