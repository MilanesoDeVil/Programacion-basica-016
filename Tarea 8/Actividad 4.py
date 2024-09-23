def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * potencia(a, b - 1)

try:
    base = float(input("Ingrese la base (a): "))
    exponente = int(input("Ingrese el exponente (b): "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es {resultado}")
except ValueError:
    print("Entrada inválida. Asegúrese de ingresar un número para la base y un entero para el exponente.")