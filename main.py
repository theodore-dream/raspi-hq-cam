from gpiozero import Button
from time import sleep
import subprocess


button17 = Button(17)
button22 = Button(22)
button23 = Button(23)
button27 = Button(27)

while True:
    if button17.is_pressed:
        print("button17 pressed")
        subprocess.call("/home/pi/Documents/raspi-hq-cam/button17.py", shell=True)
    if button22.is_pressed:
        print("button22 pressed")
        subprocess.run("/home/pi/Documents/raspi-hq-cam/button22.py", shell=True)
    if button23.is_pressed:
        print("button23 pressed")
        subprocess.run("/home/pi/Documents/raspi-hq-cam/button23.py", shell=True)
    if button27.is_pressed:
        print("button27 pressed")
    else: 
        print("released")
    sleep(0.5)

