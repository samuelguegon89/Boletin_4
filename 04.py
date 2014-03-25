for i in range(1,100):
	contador=0
	for x in range(1,i+1):
		if i % x == 0:
			contador = contador +1
	if contador <= 2 :
		print "Los numeros primos entre 0 y 100 son:",i
