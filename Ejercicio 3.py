#Desarrollar un script que solicite una frase y luego la imprima en mayusculas, minusculas y con la
#primera letra de cada palabra en mayuscula.

frase = input("Introduce una frase: ")
mayusculas = frase.upper()
minusculas = frase.lower()
capitalizado = frase.title()
print("Frase en mayúsculas:", mayusculas)
print("Frase en minúsculas:", minusculas)
print("Frase con la primera letra de cada palabra en mayúscula:", capitalizado)