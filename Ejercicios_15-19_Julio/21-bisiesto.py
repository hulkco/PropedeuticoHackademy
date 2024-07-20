"""
    Python
    link: https://www.python.org/
    Programa que:
    Crea un programa que reciba del usuario un año y le responda si es o no bisiesto
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Matemáticamente se puede saber si un año es bisiesto, si este es múltiplo de 4. Si además es múltiplo de 100 no será bisiesto (tener en cuenta que 100 es múltiplo de 4 y por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4) a no ser que sea múltiplo de 400, que sí será bisiesto.
"""

print("Calculo de año bisiesto")
print("Ingresa el año")
fecha = int(input())

if fecha % 4 == 0 and (fecha % 100 != 0 or fecha % 400 == 0):
    print("Es año bisiesto")
else:
    print("No es año bisiesto")
