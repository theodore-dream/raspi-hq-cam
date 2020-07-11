from gpiozero import Button
from time import sleep

button17 = Button(17)
button22 = Button(22)
button23 = Button(23)
button27 = Button(27)

while True:
    if button17.is_pressed:
        print("button17 pressed")
    if button22.is_pressed:
        print("button22 pressed")
    if button23.is_pressed:
        print("button23 pressed")
    if button27.is_pressed:
        print("button27 pressed")
    else: 
        print("released")
    sleep(1)

