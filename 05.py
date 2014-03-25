#!/usr/bin/env python
#-*- coding: utf-8 -*-


texto=str(raw_input("Introduzca una frase: "))

reem = texto.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u");
reem2 = reem[::-1]

if reem==reem2:
	print "Es palindroma"
else:
	print "No es palindroma"
	


