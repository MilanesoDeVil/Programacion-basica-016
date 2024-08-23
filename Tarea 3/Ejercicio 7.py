#Desarrollar un programa que lea una lista de numeros separados por
#comas y luego imprima la suma de esos numeros.

entrada = input("Introduce una lista de números separados por comas: ")
try:
    lista_str = entrada.split(',')
    lista_numeros = [float(num) for num in lista_str]
    suma = sum(lista_numeros)
    print(f"La suma de los números es: {suma:.2f}")
except ValueError:
    print("Por favor, asegúrate de que todos los elementos sean números válidos.")