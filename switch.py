from time import sleep
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
button1=16
a=0
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while(a<1):
        if GPIO.input(button1)==0:
                os.system('fswebcam -r 640x480 --jpeg 85 -D 1 fotito.jpg')

                sleep(.1)
                a=a+1
        

