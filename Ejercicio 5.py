#Crear un programa que reciba un numero flotante y lo muestre redondeado a dos decimales.

numero_str = input("Introduce un número flotante: ")
try:
  numero = float(numero_str)
  numero_redondeado = round(numero, 2)
  print(f"El número redondeado a dos decimales es: {numero_redondeado:.2f}")   

except ValueError:
 print("Por favor, introduce un número flotante válido.")