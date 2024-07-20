"""
    Ejemplos de uso de Estructuras de control en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Estructuras de control en Python
    Ciclo       
        while
"""
print("Estructuras de control en Python\n")
print("Ciclo 'while'\n")
print("Ejemplo 1: Tenemos la variable numero1=0 y mientras sea menor a 8\nimprime en la terminal su valor, sumando 1 en cada ciclo (vuelta)\n")
print("numero1 = 0\nwhile numero1 < 8:\n    numero1 += 1\n    print(numero1)\n")
numero1 = 0
while numero1 < 8:
    numero1 += 1
    print(numero1)

print("\nEjemplo 2: Tenemos la variable numero2=8 y mientras sea mayor a 0\nimprime en la terminal su valor, restando 1 en cada ciclo (vuelta)\n")
print("numero2 = 8\nwhile numero2 > 0:\n    numero2 -= 1\n    print(numero2)")
numero2 = 8
while numero2 > 0:
    numero2 -= 1
    print(numero2)

print("\nCiclo 'while' con 'else'\n")
print("Ejemplo 3: En este ejemplo se ha agregado 'else' que se\nejecutara una vez que se cumpla la primer condición\n")
print('numero3 = 8\nwhile numero3 > 0:\n    numero3 -=1\n    print(numero3)\nelse:\n    print("El bucle/ciclo ha terminado")')
numero3 = 8
while numero3 > 0:
    numero3 -=1
    print(numero3) 
else:
    print("El bucle/ciclo ha terminado")