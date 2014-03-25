Boletin_4
=========

Boletin 4 de ejercicios simples de Python.

1. Escribe un programa que determine si un número dado es par o impar. 

2. Escribe un programa para adivinar un número aleatorio. El programa generará un nú-
mero secreto aleatorio entre 0 y 100 y le preguntará al usuario por el número. Tras cada
intento el programa contestará al usuario si el número introducido es mayor o menor
que el número secreto, hasta que el usuario acierte. 

3. Escribe un programa que solicite la lectura de un texto que no contenga letras mayús-
culas. Si el usuario teclea una letra mayúscula, el programa dará un mensaje de error y
volverá a solicitar el texto. 

4. Escribe un programa que muestre los números primos comprendidos entre 1 y 100 (los
números primos son aquellos que sólo son divisibles por 1 y por ellos mismos)

5. Escribe un programa que diga si una cadena dada es un palíndromo o no. Un palíndromo
es aquella palabra o frase que se lee igual en un sentido u otro (ignorando acentos y
espacios en blanco), por ejemplo: ''Dábale arroz a la zorra el abad'' 

6. Escribe un programa para jugar al ahorcado.

◦ Un jugador introduce una palabra secreta y otro jugador tratará de adivinarla.
◦ La pantalla se limpia y aparece la horca vacía, el número de intentos y la palabra
a acertar, donde cada letra se sustituye por un asterisco.

EL JUEGO DEL AHORCADO
+−
− −+
|
|
|
|
|
|
= = = = =
= = = =
P a l a b r a a a c e r t a r : ∗∗∗∗∗∗∗∗∗∗∗
Fallos : 0
Letras utilizadas :
I n t r o d u c e una l e t r a ( ' ∗ ' p a r a r e s o l v e r ) :
◦ Reglas del juego:
· El jugador puede cometer como máximo 6 fallos. Por cada fallo aparecerá un
elemento más en la horca: cabeza, tronco, brazo izquierdo, brazo derecho,
pierna izquierda y pierna derecha
· Cada letra acertada aparecerá en la lista de letras utilizadas y se sustituirá en
la posición que corresponda en la palabra a acertar
· Una letra ya utilizada contará siempre como fallo (Esté o no en la palabra a
acertar)
2
· No se permite el uso de vocales
· El jugador puede intentar resolver la palabra a acertar en cualquier momento
tecleando la tecla *, tras lo cual se solicitará la palabra.
· El juego termina cuando el número de fallos es igual a 6 o cuando el jugador
acierta la palabra, solicitando la resolución de la misma.
· Cualquier otro carácter que se introduzca: numero o signo de puntuación, con-
tará como fallo.
◦ En un momento cualquiera el programa mostrará:
EL JUEGO DEL AHORCADO
+−
− −+
|
|
O
|
/|
|
|
|
= = = = =
= = = =
P a l a b r a a a c e r t a r : y ∗∗ t ∗p ∗∗∗ t ∗
Fallos : 3
Letras utilizadas : y n m p t b
I n t r o d u c e una l e t r a ( ' ∗ ' p a r a r e s o l v e r ) :
◦ Se obtendrá mayor puntuación en el ejercicio si se estructura adecuadamente el
código mediante el uso de funciones.
◦ Para que no se desplacen los caracteres a posiciones no deseadas, utiliza el triple
apóstrofe con el print, por ejemplo:
print ' ' '
+−
− −+
|
|
O
|
/|
|
|
|
= = = = =
= = = =
'''
◦ Para limpiar la pantalla se puede utilizar (en GNU/Linux):
i m p o r t os
os . system ( ' c l e a r ' )
