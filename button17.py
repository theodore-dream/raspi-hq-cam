from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Documents/images/image.jpg')


#cmd = "raspstill -vf -o /home/pi/Documents/images/image.jpeg"
