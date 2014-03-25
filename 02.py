import random


intervalo=random.randint(0,100)
number=-1

while number!=intervalo:
	numero=int(raw_input("Introduce un numero: "))
	if numero<intervalo:
		print "El numero es mas ALTO"
	
	elif numero>intervalo:
		print "El numero es mas BAJO"
	
	else:
		print "El numero es CORRECTO"
		break
		
