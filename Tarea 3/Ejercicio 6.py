#Escribir un programa que pida al usuario un archivo de texto y 
#luego muestre el contenido del archivo en la pantalla.

nombre_archivo = input("Introduce el nombre del archivo de texto (con extensión .txt): ")
try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encuentra en el directorio.")
except IOError:
 print(f"Hubo un problema al intentar leer el archivo '{nombre_archivo}'.")