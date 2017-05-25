import os
import sys
import smtplib
import time
import picamera
from time import sleep
import RPi.GPIO as GPIO


##Boton, Foto
GPIO.setmode(GPIO.BOARD)
button1=16
button2=15
a=0
b=0
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
##Servo
servopin=11
GPIO.setup(servopin,GPIO.OUT)
pwm=GPIO.PWM(servopin,50)

##Peajes
M_liviano= '2250'
M_pesado= '3000'
M_carga= '4500'

##Correo
smtpUser = 'labdemicros@gmail.com'
smtpPass = 'micros1234'

def send(nombre,placa,toAdd,monto):
	fromAdd= smtpUser
	subject = 'Cobro Peaje'
	header = 'Para: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
	body = 'Estimado: ' + nombre + ' se le informa que cobro del peaje MEMO 27 ha sido realizado por un monto de: '+ monto + ' colones al vehiculo de la placa: ' + placa 

	s = smtplib.SMTP('smtp.gmail.com',587)	

	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser, smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

	s.quit()


##Base de Datos
User_list=[]

class User:
	count = 0
	def __init__(self, name, plate, mail, type):
		self.name = name
		self.plate = plate
		self.mail= mail
		self.type = type
		User_list.append(self)

file=open('datos.txt','r')
lines=file.readlines()
for N in lines:
	nombre,placa,correo,tipo,empty=N.split(",")
	User(nombre,placa,correo,tipo)
file.close()

tip1="Liviano"
tip2="Pesado"
tip3="Carga"
##Verificacion de placa
def readtxt():
	archi=open('placa.txt','r')
	plate=archi.readline()
	plate=archi.readline()
	plate=plate[6:12]
	i=0
	b=0
	for N in User_list:
		i += 1
		if N.plate==plate:
			Name = N.name
			Plate = N.plate
			Mail= N.mail
			tip= N.type
			if tip == tip1:
				Monto=M_liviano
			if tip == tip2:
				Monto=M_pesado
			if tip == tip3:
				Monto=M_carga
			send(Name,Plate,Mail,Monto)
                        
			pwm.start(10)

			time.sleep(.35)
			pwm.ChangeDutyCycle(0)
			b=0
			while(b<1):
                                if GPIO.input(button2)==0:
                                        pwm.ChangeDutyCycle(.1)

					time.sleep(.35)
					pwm.ChangeDutyCycle(0)
                                        b=b+1
                                        
                        
                        break
		if i == len(User_list):
			print "Vehiculo no registrado"
	archi.close()

##Main
while(1):
        a=0
	while(a<1):
	        if GPIO.input(button1)==0:
	                with picamera.PiCamera() as picx:
                                picx.start_preview()
                                time.sleep(0.001)
                                picx.capture('foto1.jpg')
                                picx.stop_preview()
                                picx.close()
	               
                        os.system("alpr foto1.jpg >> placa.txt")
                        readtxt()
                        a=a+1

