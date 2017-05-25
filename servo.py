import RPi.GPIO as GPIO
import time 
GPIO.setmode (GPIO.BOARD)
servopin=11
GPIO.setup(servopin,GPIO.OUT)
pwm=GPIO.PWM(servopin,50)

pwm.start(10)

time.sleep(.35)
pwm.ChangeDutyCycle(0)

time.sleep(2)

pwm.ChangeDutyCycle(.1)

time.sleep(.30)
pwm.ChangeDutyCycle(0)

