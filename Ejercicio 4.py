#Hacer un programa que pida al usuario su fecha de nacimiento y
#luego imprima cuantos dias han pasado desde entonces.

from datetime import datetime
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento (en formato YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
fecha_actual = datetime.now()
diferencia = fecha_actual - fecha_nacimiento
dias_pasados = diferencia.days
print(f"Han pasado {dias_pasados} días desde tu fecha de nacimiento.")