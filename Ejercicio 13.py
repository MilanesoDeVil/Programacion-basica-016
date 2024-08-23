#Hacer un programa que pida al usuario una lista de nombres y los ordene alfabeticamente.

entrada = input("Introduce una lista de nombres separados por comas: ")
lista_nombres = [nombre.strip() for nombre in entrada.split(',')]
lista_nombres_ordenada = sorted(lista_nombres)
print("Lista de nombres ordenada alfabéticamente:")
for nombre in lista_nombres_ordenada:
    print(nombre)