#Hacer un programa que genere un numero aleatorio entre 1 y 100, y 
#pida al usuario adivinarlo, dando pistas si el numero es mayor o menor.

import random
numero_aleatorio = random.randint(1, 100)
print("He elegido un número entre 1 y 100. Intenta adivinarlo.")
adivinanza = None
while adivinanza != numero_aleatorio:
    adivinanza = int(input("Introduce tu suposición: "))
    if adivinanza < numero_aleatorio:
     print("El número es mayor. Intenta de nuevo.")
    elif adivinanza > numero_aleatorio:
     print("El número es menor. Intenta de nuevo.")
    else:
     print("¡Felicidades! Has adivinado el número.")