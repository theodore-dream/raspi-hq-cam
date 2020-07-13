#!/usr/bin/env python

# simple preview utility button

from picamera import PiCamera
from time import sleep
import time

def preview():
   camera = PiCamera()
   camera.resolution = (1920, 1080)
   camera.start_preview()
   sleep(20)
   return;

preview()
