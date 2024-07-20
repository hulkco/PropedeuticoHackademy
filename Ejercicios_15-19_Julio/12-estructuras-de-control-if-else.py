"""
    Ejemplos de uso de Estructuras de control en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Estructuras de control en Python
    Condicional
        if-else
    Ciclo 
        for           
        while
"""
print("Estructuras de control en Python")
print("Condicional 'if'")
numero1 = 2
numero2 = 4

print(f"Imprime en la terminal 'Si' numero1 '{numero1}' es mayor a numero2 '{numero2}'")

print("if numero1 > numero2:")
print('    print(f"{numero1} es mayor a {numero2}")')
print("else:")
print('     print(f"{numero1} no es mayor que {numero2}")')
print("Resultado: ")
if numero1 > numero2:
    print(f"{numero1} es mayor a {numero2}")
else: 
    print(f"{numero1} no es mayor que {numero2}")