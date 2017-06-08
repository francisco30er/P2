import os
import sys
import smtplib
import time
import picamera
from time import sleep
import RPi.GPIO as GPIO


##Boton, Se establecen los valores y comandos necesarios para el funcionamiento de los botones y servo.
GPIO.setmode(GPIO.BOARD)
button1=16 #pin 16
button2=15 #pin 15
a=0
b=0
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
##Servo
servopin=11 #pin 11
GPIO.setup(servopin,GPIO.OUT)
pwm=GPIO.PWM(servopin,50)

##Peajes, Se asignan los cobros dependiendo del tipo de vehiculo.
M_liviano= '2250'
M_pesado= '3000'
M_carga= '4500'

##Correo, Se establece el correo desde donde se enviaran las notificaciones
smtpUser = 'labdemicros@gmail.com'
smtpPass = 'micros1234'

#Se establece el correo de notificacion, asi como los parametros necesarios para enviar el mismo.
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


##Base de Datos, se establecen los datos de los usuarios.
User_list=[]

class User:
	count = 0
	def __init__(self, name, plate, mail, type):
		self.name = name
		self.plate = plate
		self.mail= mail
		self.type = type
		User_list.append(self)

#Se lee la base de datos y se asignan los datos de los usuarios.
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
	#Se lee la placa
	archi=open('placa.txt','r')
	plate=archi.readline()
	plate=archi.readline()
	plate=plate[6:12]
	i=0
	b=0
	#Se compara la placa con la base de datos para ver si existe.
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
			#Se envia el correo con la notificacion
			send(Name,Plate,Mail,Monto)
                        #Se abre la aguja
			pwm.start(10)

			time.sleep(.35)
			pwm.ChangeDutyCycle(0)
			b=0
			while(b<1):
				#Al presionarse el segundo boton se baja la aguja del peaje.
                                if GPIO.input(button2)==0:
                                        pwm.ChangeDutyCycle(.1)

					time.sleep(.35)
					pwm.ChangeDutyCycle(0)
                                        b=b+1
                                        
                                        
                                        
                        
                        break
		#Si la placa no se encuentra en la lista, se muestra el mensaje de "Vehiculo no registrado".
		if i == len(User_list):
			print "Vehiculo no registrado"
	archi.close()
	#Se borra el archivo con la placa tomada para evitar que se utilice siempre la misma.
        os.remove("placa.txt")
	
##Main
while(1):
	#Se establece que se tome la fotografia de la foto unicamente si se presiona el boton.
        a=0
	while(a<1):
	        if GPIO.input(button1)==0:
	                with picamera.PiCamera() as picx:
                                picx.start_preview()
                                time.sleep(0.001)
                                picx.capture('foto1.jpg')
                                picx.stop_preview()
                                picx.close()
	                #se captura la placa de la foto y se guarda en placa.txt
                        os.system("alpr foto1.jpg >> placa.txt")
                        readtxt()
                        a=a+1

