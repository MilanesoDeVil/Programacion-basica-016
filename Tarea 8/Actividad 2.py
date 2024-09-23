def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    numero = int(input("Ingrese un número entero no negativo para calcular el enésimo número de Fibonacci: "))
    if numero < 0:
        print("Por favor, ingrese un número no negativo.")
    else:
        print(f"El {numero}º número de Fibonacci es {fibonacci(numero)}")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")