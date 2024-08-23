#Escribir un programa que reciba una serie de calificaciones y luego imprima el promedio.

entrada = input("Introduce una serie de calificaciones separadas por comas: ")
try:
    lista_calificaciones_str = entrada.split(',')
    lista_calificaciones = [float(calificacion.strip()) for calificacion in lista_calificaciones_str]
    if lista_calificaciones:
        promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    else:
        promedio = 0 
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
except ValueError:
     print("Por favor, asegúrate de que todas las calificaciones sean números válidos.")