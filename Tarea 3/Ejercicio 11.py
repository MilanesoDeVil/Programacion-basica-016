# Desarrollar un programa que solicite al usuario su peso y altura,
# y calcule su índice de masa corporal (IMC).

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
if imc < 18.5:
    print("Categoría: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Categoría: Peso normal")
elif 25 <= imc < 29.9:
    print("Categoría: Sobrepeso")
else:
    print("Categoría: Obesidad")