User_list=[]

class User:
	count = 0
	def __init__(self, name, plate, mail, type):
		self.name = name
		self.plate = plate
		self.mail= mail
		self.type = type
		User_list.append(self)

user1 = User("Freddy Salazar","566686","freddysalazar95@gmail.com","liviano")
user2 = User("Eduardo Zuniga","566686","josedu.mec@gmail.com","pesado")
user3 = User("Randall Duran","628882","randall.d.s209@gmail.com", "liviano")
user4 = User("Franciso Elizondo","488465","asfuau","Pesadp")

def readtxt():
	archi=open('placa.txt','r')
	plate=archi.readline()
	plate=archi.readline()
	plate=plate[6:12]
	i=0
        print plate
	for N in User_list:
		i += 1
		if N.plate==plate:
			print "Name: ", N.name
			print "Plate: ", N.plate
			print "Email: ", N.mail
			print "Type: ", N.type
			break
		if i == len(User_list):
			print "Vehiculo no registrado"
	archi.close()





readtxt()
