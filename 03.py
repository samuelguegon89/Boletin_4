incorrecto=1

while incorrecto !=0:
	texto = str(raw_input("Introduce una frase: "))
	for i in texto:
		if i.islower():
			incorrecto=0
		elif i.isupper():
			incorrecto=1
			print "Hay una mayuscula en la frase, intentelo de nuevo: "
			break;
						
if incorrecto ==0:
	print "No hay mayuscula"
	print "El texto es el siguiente: ",texto
		
		
