def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    numero = int(input("Ingrese un número entero no negativo: "))
    if numero < 0:
        print("Por favor, ingrese un número no negativo.")
    else:
        print(f"El factorial de {numero} es {factorial(numero)}")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")