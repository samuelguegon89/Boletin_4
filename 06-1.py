import os
import getpass

ahorcado=['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''			
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

palabraadivinar = getpass.getpass(prompt='Jugador 1 introduzca la palabra: ')
intentos_lista = ['*']*len(palabraadivinar)
errores_malos = 0
intentos_letras = []
primer_juego = True
 
while True:
    s = ''
    for i in intentos_lista:
        s += i+','
    print ahorcado[errores_malos]
    print s[:-1]
    print "fallos: %s"% errores_malos
    print "Letras usadas : %s"% intentos_letras
    intento = raw_input('Intenta: ')
    intentos_letras.append(intento)
    os.system ('clear')
    if intento == palabraadivinar:
        print "Ganaste"
        print 'La palabra es', palabraadivinar
        break
    elif intento in palabraadivinar and len(intento)==1:
        for i in range(len(palabraadivinar)):
            if palabraadivinar[i] == intento:
                intentos_lista[i] = intento
        for i in intentos_lista:
            if i == '*':
                break
        else:
            print 'CORRECTO, La palabra es:', palabraadivinar
            break
          
    else:
        errores_malos += 1
        if errores_malos == 6:
            print "Ahorcado"
            print ahorcado[6]
            break
       
 
print "FIN del juego"
		
