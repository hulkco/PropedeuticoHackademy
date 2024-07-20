"""
    Python
    link: https://www.python.org/
    Programa que:
    Crea un programa en el que el usuario ingrese la fecha y obtenga cuantos días faltan para día de muertos y navidad
    Creado por: Gustavo Reynaga
    Julio del 2024
"""
from datetime import datetime

# Fecha de Hoy
fecha_hoy = datetime.now()

# Fechas a calcular
fecha_muertos = datetime(2024, 12, 2, 0, 0, 0)
fecha_navidad = datetime(2024, 12, 31, 0, 0, 0)
# Calcula la diferencia en dias
diferencia_muertos = fecha_muertos - fecha_hoy
diferencia_navidad = fecha_navidad - fecha_hoy

print("Faltan", 
      diferencia_muertos.days, 
      "días para el dia de muertos")
print("y", 
      diferencia_navidad.days, 
      "días para Navidad")