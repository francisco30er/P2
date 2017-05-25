import os
import sys
import smtplib
import time
from time import sleep
import RPi.GPIO as GPIO


##Boton, Foto
GPIO.setmode(GPIO.BOARD)
button1=16
a=0
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)

##Servo
servopin=11
GPIO.setup(servopin,GPIO.OUT)
pwm=GPIO.PWM(servopin,50)
##pwm.start(4)

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

user1 = User("Freddy Salazar","BGV797","freddysalazar95@gmail.com","Carga")
user2 = User("Eduardo Zuniga","845598","josedu.mec@gmail.com","Pesado")
user3 = User("Randall Duran","628882","randall.d.s209@gmail.com", "Liviano")
user4 = User("Franciso Elizondo","488465","francisco30er@gmail.com","Pesado")


##Verificacion de placa
def readtxt():
	archi=open('placa.txt','r')
	plate=archi.readline()
	plate=archi.readline()
	plate=plate[6:12]
	i=0
	for N in User_list:
		i += 1
		if N.plate==plate:
			Name = N.name
			Plate = N.plate
			Mail= N.mail
			if N.type == "Liviano":
				Monto=M_liviano
			if N.type == "Pesado":
				Monto=M_pesado
			if N.type == "Carga":
				Monto=M_carga
			send(Name,Plate,Mail,Monto)

			pwm.start(8.5)
			time.sleep(5)
			pwm.ChangeDutyCycle(4)

			break
		if i == len(User_list):
			print "Vehiculo no registrado"
	archi.close()

a=0
##Main
while(1):
	while(a<1):
	        if GPIO.input(button1)==0:
	                os.system('fswebcam -r 640x480 --jpeg 85 -D 1 fotito.jpg')
	
	                a=a+1
	os.system("alpr plate.jpg >> placa.txt")
	readtxt()
	a=0

