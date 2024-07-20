"""
    Ejemplos de uso de Estructuras de control en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Estructuras de control en Python   
    range
"""
print("Estructuras de control en Python\n")
print("El ciclo 'range' se usa para iterar en un rango de numeros predefinido\n")
print("Ejemplo 1: imprime en pantalla el ciclo 'range' de 10")
print("Nota: Se inicia desde 0 'cero'\n")
print("for i in range(10):")
print("     print(i)\n")
for i in range(10):
    print(i)
print("\nEjemplo 2: El ciclo 'range' acepta tres parametros que son: inicio, fin, salto.")
print("range(inicio, fin, salto).")
print("Si usamos 'range' con los parametros (1,12,3), se generan")
print("numeros del 1 al 12, de tres en tres\n")
print("for i in range(1,12,3):")
print("     print(i)\n")
for i in range(1,12,3):
    print(i)
print("\nComo se puede observar, no se imprime el numero final, que es 12 ")
print("Ejemplo 3: Tambien es posible hacerlo de modo inverso.")
print("Se ubica el numero mayor al inicio y el contador debe ser negativo\n")
print("for i in range(12,1,-3):")
print("     print(i)\n")
for i in range(12,1,-3):
    print(i)