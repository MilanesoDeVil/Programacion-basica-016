#Desarrollar un script que pida al usuario una oracion y cuente cuantas palabras tiene.

oracion = input("Introduce una oración: ")
palabras = oracion.split()
numero_de_palabras = len(palabras)
print(f"La oración tiene {numero_de_palabras} palabras.")