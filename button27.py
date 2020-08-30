#!/usr/bin/env python3

import time
from picamera import PiCamera


imagefolder = '/home/pi/Documents/timelapse/'

def timelapse():
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    # Finally, take several photos with the fixed settings
    for filename in camera.capture_continuous(imagefolder + 'img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(2) # wait 30 seconds

timelapse()
